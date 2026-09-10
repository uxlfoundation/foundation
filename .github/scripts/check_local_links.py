"""Check local file targets in Markdown and reStructuredText including document section anchors."""

from pathlib import Path
import io
from html import unescape
import unicodedata
from docutils.core import publish_doctree
import posixpath
import re
import sys
from urllib.parse import unquote, urlsplit

TARGETS = re.compile(
    r"(?m)^\.\. _[^\n]+?:[ \t]+([^\n]+)$"
    r"|<([^<>\n]+)>`_{1,2}"
    r'|\]\((<[^>]+>|[^)\n]+)\)'
    r"|(?m:^\[[^\]\n]+\]:[ \t]+([^\n]+)$)"
)


def anchors(path):
    content = path.read_text(encoding='utf-8')
    if path.suffix.lower() == '.rst':
        tree = publish_doctree(content, settings_overrides={
            'halt_level': 6, 'report_level': 5, 'warning_stream': io.StringIO(),
            'raw_enabled': False, 'file_insertion_enabled': False})
        return set(tree.ids)
    # GitHub heading IDs: preserve Unicode letters, remove punctuation,
    # replace spaces with hyphens, and suffix repeated headings.
    result = set(re.findall(r'<[^>]+(?:id|name)=["\']([^"\']+)', content))
    content = re.sub(r'(?ms)^(`{3,}|~{3,}).*?^\1[^\n]*$', '', content)
    lines = content.splitlines()
    for index, line in enumerate(lines):
        heading = re.match(r'^ {0,3}#{1,6}\s+(.+?)(?:\s+#+)?\s*$', line)
        title = heading.group(1) if heading else None
        if title is None and index + 1 < len(lines) and line.strip():
            if re.fullmatch(r' {0,3}(?:=+|-+)\s*', lines[index + 1]):
                title = line.strip()
        if title is None:
            continue
        title = unescape(re.sub(r'<[^>]*>', '', title))
        title = re.sub(r'!?\[([^\]]*)\]\([^)]*\)', r'\1', title).lower()
        slug = ''.join(c for c in title if c in ' -_' or unicodedata.category(c)[0] in 'LNM').replace(' ', '-')
        candidate, suffix = slug, 0
        while candidate in result:
            suffix += 1
            candidate = f'{slug}-{suffix}'
        result.add(candidate)
    return result


def check(root):
    root = root.resolve()
    entries = [p for p in root.rglob('*') if '.git' not in p.relative_to(root).parts]
    paths = {p.relative_to(root).as_posix() for p in entries}
    errors = []
    anchor_cache = {}
    for source in entries:
        if source.suffix.lower() not in {'.md', '.rst'} or not source.is_file():
            continue
        content = source.read_text(encoding='utf-8')
        for match in TARGETS.finditer(content):
            target = next(g for g in match.groups() if g is not None).strip()
            if target.startswith('<'):
                target = target[1:target.index('>')]
            else:
                target = re.split(r'\s+[\"\']', target, maxsplit=1)[0]
            if not target or target.startswith('//'):
                continue
            parsed = urlsplit(target)
            if parsed.scheme:
                continue
            local = unquote(parsed.path)
            if not local:
                local = source.name
            base = root if local.startswith('/') else source.parent
            candidate = (base / local.lstrip('/')).resolve()
            try:
                candidate.relative_to(root)
                # Keep the written case: Windows resolve() can canonicalize it.
                prefix = '' if local.startswith('/') else source.parent.relative_to(root).as_posix()
                normalized = posixpath.normpath(posixpath.join(prefix, local.lstrip('/')))
            except ValueError:
                normalized = None
            if normalized not in paths and candidate != root:
                line = content.count('\n', 0, match.start()) + 1
                errors.append(f'{source.relative_to(root).as_posix()}:{line}: missing local target: {target}')
            elif parsed.fragment and candidate.is_file() and candidate.suffix.lower() in {'.md', '.rst'}:
                if candidate not in anchor_cache:
                    anchor_cache[candidate] = anchors(candidate)
                if unquote(parsed.fragment) not in anchor_cache[candidate]:
                    line = content.count('\n', 0, match.start()) + 1
                    errors.append(f'{source.relative_to(root).as_posix()}:{line}: missing section: {target}')
    return errors


if __name__ == '__main__':
    errors = check(Path.cwd())
    for error in errors:
        print(error)
    print(f'Local documentation links: {len(errors)} error(s). External URLs and non-document fragments are not checked.')
    sys.exit(bool(errors))
