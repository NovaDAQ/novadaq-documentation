#!/usr/bin/env python3
"""Exercise the built documentation in a temporary local headless browser."""
import functools
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import threading

from playwright.sync_api import expect, sync_playwright

ROOT = Path(__file__).resolve().parents[1]


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_):
        pass


def main():
    if not (ROOT / 'site/index.html').is_file():
        raise SystemExit('Build the site with mkdocs build --strict first.')
    handler = functools.partial(QuietHandler, directory=str(ROOT / 'site'))
    server = ThreadingHTTPServer(('127.0.0.1', 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f'http://127.0.0.1:{server.server_port}'
    findings = json.loads((ROOT / 'data/findings.json').read_text())
    screenshots = ROOT / 'artifacts/browser'
    screenshots.mkdir(parents=True, exist_ok=True)
    errors = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={'width': 1440, 'height': 1000})
            page.on('pageerror', lambda error: errors.append(str(error)))
            for path, title in [
                ('index.html', 'NOvA DAQ'),
                ('packages/index.html', 'Package catalog'),
                ('review/index.html', 'Remediation priorities'),
            ]:
                response = page.goto(f'{base}/{path}')
                assert response.status == 200, path
                expect(page.locator('article h1')).to_contain_text(title)
            links = page.locator('article a[href*="github.com/NovaDAQ/"][href*="/issues/"]')
            assert links.count() == len(findings), 'Ranked register must link every GitHub issue'
            page.screenshot(path=str(screenshots / 'priorities.png'))
            page.goto(f'{base}/review/issues/NDAQ-001.html')
            expect(page.get_by_role('link', name='GitHub issue', exact=True)).to_have_attribute(
                'href', findings[0]['issue_url'])

            page.goto(f'{base}/architecture/explorer.html')
            expect(page.locator('#package-select option')).to_have_count(120)
            expect(page.locator('#dependency-summary')).to_contain_text('NovaDataLogger:')
            expect(page.locator('#dependency-graph svg')).to_be_visible()
            initial = page.locator('#dependency-table tbody tr').count()
            page.locator('#include-extra').check()
            assert page.locator('#dependency-table tbody tr').count() > initial
            page.locator('#include-extra').uncheck()
            page.locator('#package-select').select_option('TDUWeb')
            expect(page.locator('#dependency-summary')).to_contain_text('3 dependencies')
            expect(page.locator('#dependency-table tbody tr')).to_have_count(3)
            page.screenshot(path=str(screenshots / 'explorer.png'))
            page.get_by_role('link', name='Open TDUUtilities documentation', exact=True).click()
            expect(page.locator('article h1')).to_have_text('TDUUtilities')

            # Material renders Mermaid in closed shadow roots. Its replacement divs
            # and nonzero rendered heights provide the stable observable contract.
            for path, count in [('architecture/index.html', 3),
                                ('architecture/dependencies.html', 12),
                                ('operations/index.html', 1),
                                ('packages/NovaDataLogger.html', 1)]:
                page.goto(f'{base}/{path}')
                expect(page.locator('div.mermaid')).to_have_count(count, timeout=30000)
                for diagram in page.locator('div.mermaid').all():
                    expect(diagram).to_be_visible()
                    assert diagram.bounding_box()['height'] > 30, path
                if path == 'architecture/index.html':
                    page.screenshot(path=str(screenshots / 'architecture.png'))

            page.goto(f'{base}/index.html')
            search = page.get_by_role('textbox', name='Search', exact=True)
            search.fill('NDAQ-003')
            expect(page.locator('.md-search-result__link').filter(has_text='NDAQ-003')).not_to_have_count(0)
            search.press('Escape')

            page.set_viewport_size({'width': 390, 'height': 844})
            page.goto(f'{base}/architecture/explorer.html?package=TDUWeb')
            expect(page.locator('#dependency-summary')).to_contain_text('TDUWeb:')
            expect(page.locator('#package-select')).to_be_visible()
            page.screenshot(path=str(screenshots / 'mobile.png'))
            assert page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1'), 'Mobile page overflows'
            assert not errors, errors
            browser.close()
        print('Passed: catalog, ranked issue links, finding detail, explorer filters/navigation, '
              'Mermaid rendering, search, and mobile layout. Screenshots: artifacts/browser/')
    finally:
        server.shutdown()
        server.server_close()


if __name__ == '__main__':
    main()
