"""Validate RST rendering and coverage of dated records in sibling indexes."""
import io
from pathlib import Path
import re
import sys
from docutils import nodes
from docutils.core import publish_doctree


def check(root):
    errors = []
    retired = re.compile(
        r'https?://(?:spec\.oneapi\.(?:com|io)|oneapi-spec\.uxlfoundation\.org)'
        r'|https?://(?:github\.com|uxlfoundation\.github\.io)/[^\s<>]*'
        r'(?:oneapi-spec(?:[/#?]|\b)|spec-working-group)'
        r'|specification\s+working\s+group', re.IGNORECASE)
    for path in root.rglob('*'):
        if path.suffix not in {'.md', '.rst'} or '.git' in path.relative_to(root).parts:
            continue
        for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            if retired.search(line):
                errors.append(f'{path.relative_to(root)}:{number}: retired specification reference; use the UXL dynamic specification')
    for path in sorted(root.rglob('*.rst')):
        if '.git' in path.relative_to(root).parts:
            continue
        source = path.read_text(encoding='utf-8')
        tree = publish_doctree(source, settings_overrides={
            'halt_level': 6, 'report_level': 5, 'warning_stream': io.StringIO(),
            'raw_enabled': False, 'file_insertion_enabled': False,
        })
        for message in tree.findall(nodes.system_message):
            if message['level'] >= 2:
                errors.append(f'{path.relative_to(root)}:{message.get("line", "?")}: {message.astext()}')
        if re.match(r'\d{4}-\d', path.name):
            index = path.parent / 'README.rst'
            if index.exists():
                # Match actual inline links, not incidental mentions of the filename.
                links = re.findall(r'<([^<>\n]+)>`_{1,2}', index.read_text(encoding='utf-8'))
                if path.name not in links:
                    errors.append(f'{path.relative_to(root)}: missing from {index.relative_to(root)}')
    return errors


if __name__ == '__main__':
    errors = check(Path.cwd())
    for error in errors:
        print(error)
    print(f'Document structure: {len(errors)} error(s).')
    sys.exit(bool(errors))
