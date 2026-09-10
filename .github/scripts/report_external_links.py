"""On-demand, advisory external-link report; never a PR merge gate."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import os
import re
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen


def eligible(url):
    parsed = urlsplit(url)
    host = (parsed.hostname or '').lower()
    return (parsed.scheme in {'http', 'https'} and bool(host)
            and not parsed.username and not parsed.password
            and not (host == 'zoom.us' or host.endswith('.zoom.us'))
            and host not in {'docs.google.com', 'drive.google.com'}
            and not re.search(r'(?:token|password|pwd|secret|key)=', parsed.query, re.I))


def collect(root):
    references = {}
    for path in sorted(root.rglob('*')):
        if path.name == 'external-link-report.md' or path.suffix not in {'.md', '.rst'} or '.git' in path.relative_to(root).parts:
            continue
        # Operational guidance and indexes; historical minutes need a separate review.
        if re.match(r'\d{4}-\d|\d{3}-', path.name):
            continue
        for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            for url in re.findall(r'https?://[^\s<>`"\)\]]+', line):
                url = url.rstrip('.,;').split('#')[0]
                if eligible(url):
                    references.setdefault(url, []).append(f'{path.relative_to(root).as_posix()}:{number}')
    return references


def probe(url):
    try:
        request = Request(url, headers={'User-Agent': 'UXL-documentation-link-review/1.0'})
        with urlopen(request, timeout=12) as response:
            return ('reachable', str(response.status))
    except HTTPError as error:
        if error.code in {404, 410}:
            return ('missing', str(error.code))
        if error.code in {401, 403}:
            return ('restricted or bot-blocked', str(error.code))
        return ('retry or investigate', str(error.code))
    except (URLError, TimeoutError, OSError, ValueError) as error:
        return ('unverified', type(error).__name__)


def report(root):
    references = collect(root)
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = dict(zip(references, pool.map(probe, references)))
    lines = ['# External documentation link review', '',
             f'Checked {len(results)} unique URLs in guidance and indexes.', '',
             'Advisory only: 403 responses may indicate access controls or bot protection. '
             'A successful response does not verify page content or section anchors. '
             'Dated minutes, archived RFCs, PDFs, restricted recording links and Google documents are excluded.', '',
             '| Result | URL | Source |', '| --- | --- | --- |']
    for url, (status, detail) in results.items():
        if status != 'reachable':
            safe_url = url.replace('|', '%7C')
            sources = ', '.join(references[url]).replace('|', '\\|')
            lines.append(f'| {status} ({detail}) | <{safe_url}> | {sources} |')
    if all(status == 'reachable' for status, _ in results.values()):
        lines.append('| No failed requests | â€” | â€” |')
    return '\n'.join(lines) + '\n'


if __name__ == '__main__':
    result = report(Path.cwd())
    Path('external-link-report.md').write_text(result, encoding='utf-8')
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a', encoding='utf-8') as summary:
            summary.write(result)
    print(result)
