#!/usr/bin/env python3
"""Validate the committed documentation snapshot; optionally check sibling source evidence."""
import argparse
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace',type=Path)
    args=parser.parse_args()
    data=ROOT/'data';docs=ROOT/'docs'
    packages=json.loads((data/'inventory.json').read_text())
    findings=json.loads((data/'findings.json').read_text())
    edges=json.loads((data/'dependencies.json').read_text())
    coverage=json.loads((data/'coverage.json').read_text())
    names={p['name'] for p in packages}; byname={p['name']:p for p in packages}
    errors=[]
    def check(ok,message):
        if not ok: errors.append(message)
    check(len(names)==120,'Expected the 120-package reviewed snapshot')
    check({c['package'] for c in coverage}==names,'Coverage ledger does not match package inventory')
    for name in names:
        check((docs/f'packages/{name}.md').is_file(),f'Missing page: {name}')
    seen=set()
    for f in findings:
        check(f['id'] not in seen,f"Duplicate finding ID {f['id']}");seen.add(f['id'])
        check(f['package'] in names,f"Unknown finding package {f['package']}")
        check(f['severity'] in ['P0','P1','P2','P3'],f"Invalid severity {f['id']}")
        check(f['commit']==byname[f['package']]['commit'],f"Finding revision mismatch {f['id']}")
        check(bool(re.fullmatch(r'https://github\.com/NovaDAQ/'+re.escape(f['package'])+r'/issues/\d+',f.get('issue_url') or '')),
              f"Missing or mismatched GitHub issue URL: {f['id']}")
        check((docs/f"review/issues/{f['id']}.md").is_file(),f"Missing issue page {f['id']}")
        for loc in f['locations']:
            check(loc['path'] in byname[f['package']]['files'],f"Untracked evidence {f['id']} {loc['path']}")
    for e in edges:
        check(e['source'] in names and e['target'] in names,f'Unknown dependency endpoint: {e}')
        check(e['source']!=e['target'],f'Self dependency: {e}')
        check(bool(e['evidence']),f'Missing dependency evidence: {e}')
        for proof in e['evidence']:
            check(proof['path'] in byname[e['source']]['files'],f'Untracked edge source: {e}')
            check(proof['line']>0,f'Invalid edge line: {e}')
    # Resolve Markdown file links without making network requests or executing package code.
    for path in [ROOT/'README.md',*docs.rglob('*.md')]:
        text=path.read_text()
        text=re.sub(r'```.*?```','',text,flags=re.S)
        for raw in re.findall(r'\]\(([^\s)]+)\)',text):
            parsed=urlsplit(raw.strip('<>'))
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target=(path.parent/unquote(parsed.path)).resolve()
            check(target.exists(),f'Broken local link in {path.relative_to(ROOT)}: {raw}')
    if args.workspace:
        workspace=args.workspace.resolve()
        cache={}
        def source(package,path):
            key=(package,path)
            if key not in cache:
                p=workspace/package/path
                if not p.is_file():errors.append(f'Missing source {package}/{path}');return []
                cache[key]=p.read_text(errors='replace').splitlines()
            return cache[key]
        for p in packages:
            result=subprocess.run(['git','-C',str(workspace/p['name']),'rev-parse','HEAD'],text=True,capture_output=True)
            check(result.returncode==0 and result.stdout.strip()==p['commit'],f"Source HEAD differs: {p['name']}")
        for f in findings:
            for loc in f['locations']:
                lines=source(f['package'],loc['path'])
                check(0<loc['start']<=loc['end']<=len(lines),f"Invalid finding line range: {f['id']} {loc}")
                # Evidence used for issues must be unchanged relative to the recorded commit.
                result=subprocess.run(['git','-C',str(workspace/f['package']),'diff',f['commit'],'--',loc['path']],text=True,capture_output=True)
                check(result.returncode==0 and not result.stdout,f"Finding evidence has local changes: {f['id']} {loc['path']}")
        for e in edges:
            for proof in e['evidence']:
                check(proof['line']<=len(source(e['source'],proof['path'])),f'Invalid dependency source line: {e}')
    if errors:
        print('\n'.join(errors));raise SystemExit(1)
    print(f'Validated {len(names)} packages, {len(findings)} findings, {len(edges)} dependency relationships, and local Markdown links.')

if __name__=='__main__':main()
