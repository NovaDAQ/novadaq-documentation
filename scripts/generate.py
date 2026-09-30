#!/usr/bin/env python3
"""Generate the catalog and evidence-backed dependency/review pages from sibling checkouts."""
import argparse
from collections import Counter, defaultdict
import html
import json
from pathlib import Path
import re
from urllib.parse import quote

from catalog_notes import notes

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
DOCS = ROOT / 'docs'
CODE = {'.c', '.cc', '.cpp', '.cxx', '.C', '.h', '.hpp', '.py', '.sh', '.bash', '.csh', '.pl', '.m', '.v', '.vhd', '.idl'}
VENDOR = ('/Imaging-', '/lxml-', '/xlrd/', '/mikemaccana-', '/libusb', '/simplejson/', '/docs/html/', '/docs/latex/')
ALIASES = {'rms': 'ResponsiveMessagingSystem', 'SoftRelTools': 'SRT_ONLINE', 'SRT_NOVADAQ': 'SRT_ONLINE',
           'DAQHit': 'DAQHit.old', 'HoughPoint': 'HoughPoint.old', 'SimD': 'DDSSimD'}
MESSAGE_LIBS = ['RunControlMessages', 'GlobalTriggerMessages', 'DDTTriggerMessages', 'DAQDCSMessages',
                'DAQDCSMonitorMessages', 'ErrorHandlerMessages', 'NssMessages', 'NSNMessages',
                'SNEWSMessages', 'SpillServerMessages', 'SuperNovaMessages']
ALIASES.update({k: 'DAQMessages' for k in MESSAGE_LIBS})
SEVERITY = {'P0': 'Critical', 'P1': 'High', 'P2': 'Medium', 'P3': 'Low'}

def dump(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + '\n')

def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + '\n')

def link(pkg, path, line=None):
    url = f"https://github.com/NovaDAQ/{pkg['name']}/blob/{pkg['commit']}/{quote(path)}"
    return f"[{path}{':' + str(line) if line else ''}]({url}{'#L' + str(line) if line else ''})"

def test_path(path):
    return bool(re.search(r'(^|/)(test|tests|unittest|demo|demos|examples?)(/|$)', path))

def in_scope(name, path):
    if any(token in '/' + path for token in VENDOR):
        return False
    if name == 'DCMBootLoader':
        return '/novadcm/' in path or not path.startswith('ecos/') or path == 'ecos/setup'
    if name == 'linux_kernel_dcmtdu':
        return path in ['Makefile', 'README', 'arch/powerpc/platforms/83xx/mpc834x_itx.c'] or (
            path.startswith(('arch/powerpc/configs/', 'arch/powerpc/boot/dts/')) and
            any(x in path.lower() for x in ['dcm', 'tdu', '834']))
    return True

def resolve(token, names):
    if token in names:
        return token
    if token in ALIASES:
        return ALIASES[token]
    if token.startswith('DatabaseUtils'):
        return 'DatabaseUtils'
    if token == 'NovaResourceManagerXSD':
        return 'NovaResourceManager'
    return None

def build_inventory(workspace, packages):
    names = {p['name'] for p in packages}
    edges = defaultdict(list)
    catalogs = {}
    for p in packages:
        name = p['name']
        cat = dict(build_files=[], headers=[], entrypoints=[], configs=[], tests=[], readmes=[],
                   env={}, external_includes={}, source_files=[], inspected_files=[])
        for f in p['files']:
            path = workspace / name / f
            if not path.is_file():
                continue
            suffix = Path(f).suffix
            base = Path(f).name
            if not in_scope(name, f):
                continue
            build = base in ['GNUmakefile', 'Makefile', 'CMakeLists.txt', 'product_deps'] or suffix in ['.mk', '.pro']
            if build:
                cat['build_files'].append(f)
            if base.upper().startswith('README') or (f.startswith('doc/') and suffix in ['.md', '.txt', '.tex']):
                cat['readmes'].append(f)
            if suffix in ['.xml', '.xsd', '.idl', '.fcl', '.conf', '.ini', '.yaml', '.yml', '.json']:
                cat['configs'].append(f)
            if suffix in CODE:
                cat['source_files'].append(f)
            if test_path(f) and suffix in CODE:
                cat['tests'].append(f)
            if suffix not in CODE and not build and not (name == 'setup' and 'packages-' in f):
                continue
            if path.stat().st_size > 2_000_000:
                continue
            try:
                text = path.read_text(errors='replace')
            except OSError:
                continue
            if '\x00' in text:
                continue
            cat['inspected_files'].append(f)
            # Class/struct declarations are a source-linked API map, not generated ABI documentation.
            if suffix in ['.h', '.hpp'] and not test_path(f):
                symbols = re.findall(r'^\s*(?:class|struct|enum(?:\s+class)?)\s+([A-Za-z_]\w*)', text, re.M)
                cat['headers'].append(dict(path=f, symbols=sorted(set(symbols))))
            if not test_path(f):
                if re.search(r'\b(?:int|void)\s+main\s*\(', text) or (
                    suffix in ['.sh', '.bash', '.csh', '.pl', '.py'] and
                    (text.startswith('#!') or '__main__' in text or '/script' in '/' + f or '/bin/' in '/' + f)):
                    cat['entrypoints'].append(f)
            for n, raw in enumerate(text.splitlines(), 1):
                # Do not publish values of environment variables, passwords, or arbitrary script lines.
                for env in re.findall(r'(?:getenv\s*\(|environ\.get\s*\(|environ\s*\[)\s*[\'\"]([A-Z][A-Z0-9_]*)', raw):
                    cat['env'].setdefault(env, dict(path=f, line=n))
                incl = re.match(r'\s*#\s*include\s*[<\"]([^>\"]+)', raw)
                if incl:
                    token = incl.group(1).split('/')[0]
                    dep = resolve(token, names)
                    if dep and dep != name:
                        kind = 'test include' if test_path(f) else 'source include'
                        edges[(name, dep, kind)].append(dict(path=f, line=n))
                    elif not dep and '/' in incl.group(1):
                        cat['external_includes'].setdefault(token, dict(path=f, line=n))
                if build and not raw.lstrip().startswith('#'):
                    if re.search(r'\binclude\s+SoftRelTools/', raw) and name != 'SRT_ONLINE':
                        edges[(name, 'SRT_ONLINE', 'build tool')].append(dict(path=f, line=n))
                    for token in re.findall(r'(?:^|\s)-l\s*([A-Za-z_]\w*)', raw):
                        dep = resolve(token, names)
                        if dep and dep != name:
                            kind = 'test link' if test_path(f) else 'build link'
                            edges[(name, dep, kind)].append(dict(path=f, line=n))
                if name == 'setup' and 'packages-' in f and not raw.lstrip().startswith('#'):
                    tok = raw.split()
                    dep = resolve(tok[0], names) if tok else None
                    if dep and dep != name:
                        edges[(name, dep, 'release manifest')].append(dict(path=f, line=n))
            if base == 'CMakeLists.txt':
                # Preserve offsets so every dependency points to its own source token.
                clean = re.sub(r'(?m)#.*$', lambda m: ' ' * len(m.group()), text)
                for m in re.finditer(r'\bLIBRARIES\s+([^)]*)', clean):
                    for token in re.finditer(r'\b[A-Za-z_]\w*\b', m.group(1)):
                        dep = resolve(token.group(), names)
                        if dep and dep != name:
                            # Locate the source token in original text for an inspectable evidence link.
                            at = m.start(1) + token.start()
                            n = text[:at].count('\n') + 1
                            kind = 'test link' if test_path(f) else 'build link'
                            edges[(name, dep, kind)].append(dict(path=f, line=n))
        catalogs[name] = cat
    # Explicit command invocations: verified operational relationships, not inferred from prose.
    runtime = [
        ('TDUWeb','TDUUtilities','server/tdu_webserver.py',22),
        ('TDUWeb','SHM_Utilities','server/tdu_webserver.py',10),
        ('TDUWeb','NovaSpillServer','server/tdu_webserver.py',58),
        ('NovaDAQLiveTimeMonitor','ShmRdWr','py/DAQLiveTimeMonitor.py',247),
    ]
    for source, target, path, line in runtime:
        edges[(source,target,'runtime command')].append(dict(path=path,line=line))
    result = []
    for (source,target,kind), evidence in sorted(edges.items()):
        unique = {(e['path'],e['line']):e for e in evidence}
        result.append(dict(source=source,target=target,kind=kind,evidence=list(unique.values())))
    return catalogs, result

def mermaid(nodes, edges):
    ids = {name:f'p{i}' for i,name in enumerate(sorted(nodes))}
    lines = ['flowchart LR']
    lines += [f'  {ids[n]}["{n}"]' for n in sorted(nodes)]
    pairs = set()
    for e in edges:
        pair = (e['source'],e['target'])
        if pair in pairs or pair[0] not in ids or pair[1] not in ids:
            continue
        pairs.add(pair)
        lines.append(f'  {ids[pair[0]]} --> {ids[pair[1]]}')
    return '\n'.join(lines)

def table(headers, rows):
    def cell(s):
        return str(s).replace('|','\\|').replace('\n',' ')
    return '\n'.join(['| '+' | '.join(headers)+' |', '| '+' | '.join(['---']*len(headers))+' |'] +
                     ['| '+' | '.join(cell(v) for v in row)+' |' for row in rows]) + '\n'

def generate(workspace):
    packages = json.loads((DATA/'inventory.json').read_text())
    findings = json.loads((DATA/'findings.json').read_text())
    scan = json.loads((DATA/'static-analysis.json').read_text())
    curated = notes()
    assert set(curated) == {p['name'] for p in packages}
    byname = {p['name']:p for p in packages}
    catalogs, edges = build_inventory(workspace, packages)
    dump(DATA/'catalog.json', catalogs)
    dump(DATA/'dependencies.json', edges)
    dump(DATA/'package-notes.json', curated)
    dump(DOCS/'assets/dependencies.json', {'packages':{n:dict(v,commit=byname[n]['commit']) for n,v in curated.items()}, 'edges':edges})
    issue_by_pkg = defaultdict(list)
    for f in findings:
        issue_by_pkg[f['package']].append(f)
    cpp = Counter(f.split('/')[0] for f in scan['cppcheck']['files'])
    shell = Counter(f.split('/')[0] for f in scan['shellcheck']['files'])
    py = Counter(f['file'].split('/')[0] for f in scan['python']['files'])
    coverage = []
    # Exclude test-only edges, build tooling, and release membership from runtime/source overview diagrams.
    core_edges = [e for e in edges if e['kind'] in ['source include','build link','runtime command']]
    for p in packages:
        name = p['name']; cat = catalogs[name]; note = curated[name]
        deps = [e for e in edges if e['source']==name]
        users = sorted({e['source'] for e in core_edges if e['target']==name})
        local = [e for e in core_edges if e['source']==name]
        sources = sorted({e['target'] for e in local})
        lines = [f'# {name}', note['purpose'], '## Identity and scope',
                 f"Repository: [NovaDAQ/{name}](https://github.com/NovaDAQ/{name}) · Reviewed commit: `{p['commit']}` · Domain: **{note['group']}**.",
                 f"Tracked files: **{len(p['files'])}**. Production deployment and owner are **unconfirmed**." +
                 (' The directory name marks a legacy variant; retirement has not been independently verified.' if name.endswith(('_OLD','.old')) else '')]
        if p['status']:
            lines.append('This checkout had pre-existing local changes. Remote source links identify the committed revision; local changes were preserved. See the snapshot ledger for affected paths.')
        lines += ['## Operation',note['operations'],
                  'For prerequisites, safe start/stop sequencing, health checks, and rollback see the [operations guide](../operations/index.md).',
                  '## Build and integration']
        builds = cat['build_files']
        if 'GNUmakefile' in builds:
            lines.append('This package uses the SRT/SoftRelTools release context. A standalone `make` in a fresh checkout is not a supported build recipe unless the required context is already configured. See [build and release](../operations/build.md).')
        if 'CMakeLists.txt' in builds:
            lines.append('CMake definitions are present. Most NOvA fragments use parent-provided cetbuildtools macros and dependency targets; consult the files below before treating this directory as a standalone CMake project.')
        if not builds:
            lines.append('No supported make/CMake build definition was found in the scoped inventory. Use the source-linked entry points and existing package instructions; do not infer a missing build command.')
        lines += [table(['Build definition'],[(link(p,f),) for f in builds]) if builds else '',
                  '## Entry points',
                  'These are source entry points or operational scripts found statically. Installation names and enabled targets depend on the build/configuration; listing a script does not establish that it is deployed.']
        lines.append(table(['Source'],[(link(p,f),) for f in cat['entrypoints']]) if cat['entrypoints'] else 'No standalone executable entry point was identified; this package may provide libraries, contracts, configuration, or binary artifacts.')
        lines += ['## Interfaces',
                  'Headers and declared types form the API navigation map. Follow the source for method signatures, ownership, units, and error contracts. Generated DDS/XSD types are built from the schemas in the next section.']
        lines.append(table(['Header','Declared types'],[(link(p,h['path']),', '.join(f'`{s}`' for s in h['symbols']) or 'Functions, constants, or templates') for h in cat['headers']]) if cat['headers'] else 'No public C/C++ header was identified in the scoped inventory. Script and schema interfaces are linked elsewhere on this page.')
        lines += ['## Configuration and data contracts']
        lines.append(table(['Source artifact'],[(link(p,f),) for f in cat['configs']]) if cat['configs'] else 'No separate XML/IDL/XSD/FHiCL/INI/YAML/JSON configuration was identified. Inspect command-line parsing and site launchers for this package; defaults may be embedded in source.')
        lines += ['## Environment and external dependencies',
                  'Environment names below are literal lookups found in source, not a guarantee that every value is mandatory. No environment values or credentials are copied into this documentation.']
        lines.append(table(['Variable','Evidence'],[(f'`{env}`',link(p,e['path'],e['line'])) for env,e in sorted(cat['env'].items())]) if cat['env'] else 'No literal environment lookup was identified by this scan; shell setup scripts may still provide required values.')
        if cat['external_includes']:
            lines += ['Unresolved/non-package include roots (some are system or generated headers; this is not a package-manager lockfile):',
                      table(['Include root','Evidence'],[(f'`{key}`',link(p,e['path'],e['line'])) for key,e in sorted(cat['external_includes'].items())])]
        lines += ['## Package dependencies',
                  'Arrow direction is **consumer → dependency**. This diagram includes source/build/runtime relationships and excludes test-only, release-membership, and build-tool edges. Conditional branches are not evaluated.']
        if local:
            lines.append('```mermaid\n'+mermaid({name,*sources},local)+'\n```')
        else:
            lines.append('No cross-package source/build/runtime edge was resolved in the scoped inventory. This does not imply the package has no external or operational dependencies.')
        lines.append(table(['Dependency','Relationship','Evidence'],[(f"[{e['target']}]({e['target']}.md)",e['kind'],link(p,e['evidence'][0]['path'],e['evidence'][0]['line'])) for e in deps]) if deps else '')
        lines += ['Direct consumers: '+(', '.join(f'[{n}]({n}.md)' for n in users) or 'None resolved in this snapshot')+'.',
                  'Explore upstream/downstream impact in the [dependency explorer](../architecture/explorer.md).',
                  '## Validation and review',
                  f"Static analysis attempted **{cpp[name]} C/C++ translation units**, **{shell[name]} shell scripts**, and parsed **{py[name]} Python files**. Counts are tool input coverage, not proof of successful compilation or exhaustive review. Source/build/configuration inventories and the operating surface were also assessed."]
        if name in ['linux_kernel_dcmtdu','DCMBootLoader','FEBCheckoutVerify','DDSSimD','DCMulator']:
            lines.append('Large vendor/generated/firmware trees received a bounded integration review. The [methodology](../review/methodology.md) records exclusions. No complete third-party audit or hardware validation is claimed.')
        if issue_by_pkg[name]:
            lines.append(table(['Severity','Finding','GitHub'],[(f['severity'],f"[{f['id']}: {f['title']}](../review/issues/{f['id']}.md)",f"[Issue]({f['issue_url']})" if f['issue_url'] else 'Pending') for f in issue_by_pkg[name]]))
        else:
            lines.append('No actionable defect was confirmed for this package in this review. This is a bounded review result, not a clean bill of health; unvalidated analyzer diagnostics were not filed as bugs.')
        lines += ['Existing test/example sources (not executed against production):',
                  table(['Source'],[(link(p,f),) for f in cat['tests']]) if cat['tests'] else 'No test/example source identified in the scoped inventory.',
                  '## Existing documentation',
                  table(['Source'],[(link(p,f),) for f in cat['readmes']]) if cat['readmes'] else 'No package README/manual identified in the scoped inventory. Use this page and the source interfaces above.']
        write(DOCS/f'packages/{name}.md','\n\n'.join(l for l in lines if l))
        coverage.append(dict(package=name,commit=p['commit'],tracked_files=len(p['files']),
                             scoped_text_files=len(cat['inspected_files']),cpp_inputs=cpp[name],shell_inputs=shell[name],
                             python_parsed=py[name],findings=[f['id'] for f in issue_by_pkg[name]],
                             scope='bounded integration' if name in ['linux_kernel_dcmtdu','DCMBootLoader','FEBCheckoutVerify','DDSSimD','DCMulator'] else 'static package review'))
    dump(DATA/'coverage.json',coverage)
    groups = sorted({n['group'] for n in curated.values()})
    index = ['# Package catalog',f'All **{len(packages)}** sibling repositories are included. Descriptions are source-derived; production ownership/lifecycle remains to be confirmed.']
    for group in groups:
        index += [f'## {group}', table(['Package','Purpose','Findings'],[(f"[{p['name']}]({p['name']}.md)",curated[p['name']]['purpose'],len(issue_by_pkg[p['name']])) for p in packages if curated[p['name']]['group']==group])]
    write(DOCS/'packages/index.md','\n\n'.join(index))
    write(DOCS/'review/coverage.md','# Review coverage\n\nEvery repository was inventoried and its scoped code/build/operational surface assessed. Static-analysis input counts below do not imply every file was manually read or successfully parsed. No DAQ binary, hardware test, or live service was run.\n\n'+
          table(['Package','Scope','C/C++ inputs','Shell inputs','Python parsed','Confirmed issues'],[(f"[{c['package']}](../packages/{c['package']}.md)",c['scope'],c['cpp_inputs'],c['shell_inputs'],c['python_parsed'],', '.join(c['findings']) or 'None confirmed') for c in coverage]))
    snapshot = ['# Reviewed snapshot','Snapshot date: **2026-09-30**. Remote source links are pinned to these commits. All source repositories were private at review time. Working changes were preserved.']
    snapshot.append(table(['Repository','Commit','Pre-existing local changes'],[(f"[{p['name']}](../packages/{p['name']}.md)",f"`{p['commit']}`",'Yes' if p['status'] else 'No') for p in packages]))
    for p in packages:
        if p['status']:
            snapshot += [f"## {p['name']}",'```text\n'+p['status']+'\n```']
    write(DOCS/'review/snapshot.md','\n\n'.join(snapshot))
    ranking = sorted(findings,key=lambda f:(f['severity'], -len({e['source'] for e in core_edges if e['target']==f['package']}),f['id']))
    counts = Counter(f['severity'] for f in findings)
    review = ['# Remediation priorities',
              f"**{len(findings)} confirmed findings** across **{len({f['package'] for f in findings})} repositories**. "+', '.join(f"{p}: {counts[p]} {SEVERITY[p].lower()}" for p in SEVERITY)+'.',
              'Use impact severity first, then confirm deployment, direct consumers, reproduction frequency, and change risk. Effort is a rough scope estimate: S = local change; M = coordinated or multi-path change; L = redesign. It is not a delivery commitment.',
              '## Severity scale',table(['Rank','Meaning','Suggested handling'],[
                  ('P0 — Critical','Verified immediate, widespread critical failure with no practical containment','Interrupt normal work; contain immediately'),
                  ('P1 — High','Data corruption/loss, kernel or data-path failure, or unauthorized hardware effects under a stated trigger','Confirm deployment promptly; contain and fix before the next affected operation'),
                  ('P2 — Medium','Bounded functional failure, recovery failure, incorrect diagnostics, or resource leakage','Schedule a targeted fix and regression validation'),
                  ('P3 — Low','Limited operational impact with a practical workaround','Batch with nearby maintenance')]),
              '## Recommended sequence',
              '1. Confirm active deployments and contain hardware/control exposure: TDUWeb, PowerUtilities, and dcm_kernel_module.\n2. Protect data and build integrity: NovaDataLogger, BufferNodeEVB, RawFileParser, ShmRdWr, MetaDataTools, and ups.\n3. Repair shared messaging and lifecycle defects, then validate representative consumers.\n4. Repair transfer/catalog handling and operational scripts; reconcile affected data/metadata.\n5. Reproduce historical/legacy issues only after identifying an active consumer or archival requirement.',
              '## Ranked issue register',
              'GitHub status is a snapshot. Run `python scripts/publish_issues.py --refresh` and regenerate to update it. The complete trigger, recommendation, and acceptance criteria are in each finding page.',
              table(['Rank','Package / finding','Impact','Direct consumers','Scope','GitHub'],[
                  (f['severity'],f"[{f['id']}: {f['package']} — {f['title']}](issues/{f['id']}.md)",f['impact'],
                   len({e['source'] for e in core_edges if e['target']==f['package']}),f['effort'],
                   f"[{f['status']}]({f['issue_url']})" if f['issue_url'] else 'Pending') for f in ranking]),
              '## Closing an issue',
              'Record the deployed consumer and reproduction, implement the smallest complete correction, run the acceptance cases in the issue, and verify a representative integration path. Attach the fixed commit and validation evidence before closing. If retired, document the retirement decision and replacement; do not imply the defect was fixed.',
              '[Coverage](coverage.md) · [Methodology and limitations](methodology.md) · [Reviewed revisions](snapshot.md)']
    write(DOCS/'review/index.md','\n\n'.join(review))
    depdoc = ['# Package dependencies','Arrow direction: **consumer → dependency**. Edges are extracted from literal includes, linker declarations, SoftRelTools references, selected runtime commands, and release manifests. Conditional/optional/test relationships are retained as separate types in the evidence table. This is not a resolved linker graph or a claim about deployed topology.',
              f'The snapshot contains **{len(packages)} packages** and **{len(edges)} typed relationships**. Use the [interactive explorer](explorer.md) for a focused graph, the individual package pages for immediate dependencies, or the [full Mermaid source](dependencies.mmd) for export.',
              '## Subsystem views','These diagrams show relationships whose source and target are both inside a domain. Cross-domain relationships remain in the complete evidence table and explorer. Build tools and test-only edges are omitted from these views.']
    for group in groups:
        nodes = {n for n,note in curated.items() if note['group']==group}
        subset = [e for e in core_edges if e['source'] in nodes and e['target'] in nodes]
        depdoc += [f'### {group}','```mermaid\n'+mermaid(nodes,subset)+'\n```']
    depdoc += ['## Relationship evidence',table(['Consumer','Dependency','Type','First evidence','Occurrences'],[
        (f"[{e['source']}](../packages/{e['source']}.md)",f"[{e['target']}](../packages/{e['target']}.md)",e['kind'],
         link(byname[e['source']],e['evidence'][0]['path'],e['evidence'][0]['line']),len(e['evidence'])) for e in edges])]
    write(DOCS/'architecture/dependencies.md','\n\n'.join(depdoc))
    write(DOCS/'architecture/dependencies.mmd',mermaid(set(byname),core_edges))
    nav = ['site_name: NOvA DAQ Documentation','site_description: Package reference, operations, dependencies, and review priorities',
           'repo_url: https://github.com/NovaDAQ/novadaq-documentation','use_directory_urls: false',
           'theme:','  name: material','  font: false','  features:','    - navigation.tabs','    - navigation.top','    - content.code.copy',
           'plugins:','  - search','markdown_extensions:','  - tables','  - admonition','  - attr_list','  - pymdownx.details',
           '  - pymdownx.superfences:','      custom_fences:','        - name: mermaid','          class: mermaid','          format: !!python/name:pymdownx.superfences.fence_code_format',
           'extra_javascript:','  - assets/explorer.js','extra_css:','  - assets/style.css',
           'validation:','  nav:','    omitted_files: info','  links:','    not_found: warn','    unrecognized_links: warn',
           'nav:','  - Home: index.md','  - Review:','      - Priorities: review/index.md','      - Coverage: review/coverage.md','      - Methodology: review/methodology.md','      - Validation: review/validation.md','      - Snapshot: review/snapshot.md',
           '  - Architecture:','      - System: architecture/index.md','      - Dependencies: architecture/dependencies.md','      - Explorer: architecture/explorer.md',
           '  - Operations:','      - Runbook: operations/index.md','      - Build and release: operations/build.md','      - Recovery: operations/recovery.md',
           '  - Packages:','      - Catalog: packages/index.md']
    for group in groups:
        nav.append(f'      - {group}:')
        nav.extend(f"          - {name}: packages/{name}.md" for name in sorted(curated) if curated[name]['group']==group)
    nav += ['  - Maintaining this suite: contributing.md']
    write(ROOT/'mkdocs.yml','\n'.join(nav))
    print(f'Generated {len(packages)} package pages, {len(edges)} relationships, {len(findings)} ranked findings.')

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace',type=Path,default=ROOT.parent)
    generate(parser.parse_args().workspace.resolve())
