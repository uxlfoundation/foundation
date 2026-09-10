"""Advisory review of added files; existing assets and detected renames are excluded."""
import os
import subprocess

LIMIT = 10 * 1024 * 1024


def large_additions(base, head='HEAD'):
    names = subprocess.check_output([
        'git', 'diff', '--name-only', '-z', '--diff-filter=A', '-M',
        f'{base}...{head}'], text=True).split('\0')
    findings = []
    for name in filter(None, names):
        size = int(subprocess.check_output(['git', 'cat-file', '-s', f'{head}:{name}']))
        if size > LIMIT:
            findings.append((name, size))
    return findings


if __name__ == '__main__':
    findings = large_additions(os.environ['BASE_SHA'], os.environ['HEAD_SHA'])
    lines = ['## New attachment review', '',
             'Advisory: added files over 10 MiB may be better shared as hosted links.',
             'Existing files and detected renames are excluded.', '']
    lines += [f'- `{name}`: {size / 1024 / 1024:.1f} MiB' for name, size in findings]
    if not findings:
        lines.append('No new files over 10 MiB.')
    report = '\n'.join(lines) + '\n'
    print(report)
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a', encoding='utf-8') as stream:
            stream.write(report)
