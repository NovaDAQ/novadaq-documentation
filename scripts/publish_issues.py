#!/usr/bin/env python3
"""Publish verified findings, using stable markers to avoid duplicate issues."""
import argparse
import json
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data/findings.json'
SEVERITY = {'P0': 'Critical', 'P1': 'High', 'P2': 'Medium', 'P3': 'Low'}

def gh(*args):
    return subprocess.check_output(['gh', *args], text=True).strip()

def body(f):
    sources = '\n'.join(
        f"- [{l['path']}:{l['start']}](https://github.com/NovaDAQ/{f['package']}/blob/"
        f"{f['commit']}/{l['path']}#L{l['start']}-L{l['end']})" for l in f['locations'])
    return f"""<!-- novadaq-review:{f['id']} -->
Severity: **{f['severity']} — {SEVERITY[f['severity']]}** · Estimated scope: **{f['effort']}**

Reviewed revision: `{f['commit']}`. Source review dated 2026-09-30.

### Trigger and evidence

{f['trigger']}

{sources}

### Impact

{f['impact']}

### Recommended change

{f['fix']}

### Validation / acceptance criteria

{f['validation']}

The defect was verified by source inspection; any executed reproductions are explicitly identified above. Production hardware and services were not exercised. Severity describes potential impact; deployment status should determine scheduling.

Tracking ID: `{f['id']}`. Central review and package documentation: `novadaq-documentation`.
"""

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true', help='Create missing issues on GitHub')
    parser.add_argument('--refresh', action='store_true', help='Refresh states of existing issues')
    args = parser.parse_args()
    rows = json.loads(DATA.read_text())
    cached = {}
    issue_dir = ROOT / 'docs/review/issues'
    issue_dir.mkdir(parents=True, exist_ok=True)
    for f in rows:
        content = body(f)
        repo = f"NovaDAQ/{f['package']}"
        if f['issue_url']:
            if args.refresh:
                state = json.loads(gh('issue', 'view', f['issue_url'], '--json', 'state,updatedAt'))
                f['status'] = state['state'].lower()
                f['github_updated_at'] = state['updatedAt']
            continue
        if not args.apply:
            print(f"Draft {f['id']}: [{f['severity']}] {f['title']}")
            continue
        if repo not in cached:
            # Pagination includes closed issues: do not reopen or duplicate a previously resolved finding.
            pages = json.loads(gh('api', '--paginate', '--slurp', f'repos/{repo}/issues?state=all&per_page=100'))
            cached[repo] = [i for page in pages for i in page if 'pull_request' not in i]
        marker = f"<!-- novadaq-review:{f['id']} -->"
        existing = next((i for i in cached[repo] if marker in (i.get('body') or '')
                         or i['title'] == f"[{f['severity']}] {f['title']}"), None)
        if existing:
            f['issue_url'] = existing['html_url']
            f['status'] = existing['state']
        else:
            # Body is passed as file contents, never interpolated into a shell command.
            with tempfile.TemporaryDirectory(prefix='novadaq-issue-') as temp:
                path = Path(temp) / 'body.md'
                path.write_text(content)
                f['issue_url'] = gh('issue', 'create', '--repo', repo, '--title',
                                    f"[{f['severity']}] {f['title']}", '--body-file', str(path))
            f['status'] = 'open'
        # Save after each remote mutation so an interrupted run can resume safely.
        DATA.write_text(json.dumps(rows, indent=2) + '\n')
        print(f"{f['id']} {f['issue_url']}", flush=True)
    DATA.write_text(json.dumps(rows, indent=2) + '\n')
    for f in rows:
        tracking = (f"[GitHub issue]({f['issue_url']}) · Status: **{f['status']}** · "
                    if f['issue_url'] else '')
        (issue_dir / (f['id'] + '.md')).write_text(
            f"# {f['id']}: {f['title']}\n\n" + tracking +
            "[Remediation priorities](../index.md)\n\n" + body(f))

if __name__ == '__main__':
    main()
