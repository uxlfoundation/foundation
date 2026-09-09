"""Check local file targets in Markdown and reStructuredText (not URL/anchors)."""

from pathlib import Path
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


def check(root):
    root = root.resolve()
    entries = [p for p in root.rglob('*') if '.git' not in p.relative_to(root).parts]
    paths = {p.relative_to(root).as_posix() for p in entries}
    errors = []
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
            if not target or target.startswith(('#', '//')):
                continue
            parsed = urlsplit(target)
            if parsed.scheme:
                continue
            local = unquote(parsed.path)
            if not local:
                continue
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
    return errors


if __name__ == '__main__':
    errors = check(Path.cwd())
    for error in errors:
        print(error)
    print(f'Local documentation links: {len(errors)} error(s). External URLs and anchors are not checked.')
    sys.exit(bool(errors))
