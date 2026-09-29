#!/usr/bin/env python3
"""Validate tracked M0 files; no network, deployment, or third-party dependency."""
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

REQUIRED = {
    'README.md', 'CONTRIBUTING.md', '.gitignore',
    'documentation/repository-conventions.md',
    'documentation/project-governance/project-status.md',
    'documentation/installation/installation-guide.md',
    'documentation/operations/operations-readiness.md',
    'documentation/hosting/hosting-comparison.md',
    'documentation/quality/test-strategy.md',
}
SPECIAL = {'README.md', 'CONTRIBUTING.md', '.gitignore', '.env.example',
           'pull_request_template.md', '.github'}
ALLOWED_ROOTS = {'applications', 'configuration', 'documentation', 'infrastructure',
                 'shared-packages', 'services', 'tests', 'scripts', '.github'}
PRIVATE_KEY = re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH |DSA |ENCRYPTED )?PRIVATE KEY-----')


def contains_symlink(path: Path) -> bool:
    """Inspect lexical components before resolve() can hide a local alias."""
    return path.is_symlink() or any(parent.is_symlink() for parent in path.parents)


def inspect(root: Path, paths: list[str], require_layout: bool = True) -> list[str]:
    root = root.resolve()
    errors = []
    tracked = {root / name for name in paths}
    if require_layout:
        errors.extend(f'Missing required file: {p}' for p in sorted(REQUIRED - set(paths)))
    for name in paths:
        path = root / name
        parts = Path(name).parts
        if contains_symlink(path) or root not in path.resolve().parents:
            errors.append(f'Unsupported symlink or escaping path: {name}')
            continue
        if len(parts) > 1 and parts[0] not in ALLOWED_ROOTS:
            errors.append(f'Unregistered root directory: {name}')
        for component in parts:
            valid = bool(re.fullmatch(r'[a-z0-9]+(?:[-.][a-z0-9]+)*', component))
            if component.endswith('.py'):
                valid = bool(re.fullmatch(r'[a-z0-9]+(?:_[a-z0-9]+)*\.py', component))
            if component not in SPECIAL and not valid:
                errors.append(f'Invalid name: {name}')
        if any(re.fullmatch(r'(?:misc|divers|new|temp|final\d+)(?:\..*)?', p) for p in parts):
            errors.append(f'Ambiguous name: {name}')
        forbidden = (path.name.startswith('.env') and path.name != '.env.example') or (
            path.suffix.lower() in {'.pem', '.key', '.p12', '.pfx', '.dump', '.backup', '.bak'}
        ) or any(p in {'node_modules', 'backups', 'production-data', '__pycache__'} for p in parts)
        if forbidden:
            errors.append(f'Forbidden tracked file: {name}')
        try:
            body = path.read_text(encoding='utf-8')
        except (OSError, UnicodeDecodeError):
            errors.append(f'Unreadable/non-text file in documentation baseline: {name}')
            continue
        if PRIVATE_KEY.search(body):
            errors.append(f'Private-key marker detected (value withheld): {name}')
        if path.suffix != '.md':
            continue
        body = re.sub(r'(?ms)^```.*?^```[^\n]*$', '', body)
        for target in re.findall(r'!?\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)', body):
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            candidate = path.parent / unquote(url.path)
            if contains_symlink(candidate):
                errors.append(f'Unsupported symlink in local link: {name} -> {target}')
                continue
            destination = candidate.resolve()
            if destination != root and root not in destination.parents:
                errors.append(f'Link escapes repository: {name} -> {target}')
            elif not destination.exists():
                errors.append(f'Broken local link: {name} -> {target}')
            elif destination.is_dir():
                if not any(destination in item.parents for item in tracked):
                    errors.append(f'Link directory has no tracked content: {name} -> {target}')
            elif destination not in tracked:
                errors.append(f'Link target is not tracked: {name} -> {target}')
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    paths = subprocess.check_output(['git', 'ls-files', '-z'], cwd=root).decode().split('\0')
    paths = [p for p in paths if p]
    errors = inspect(root, paths)
    for error in errors:
        print(f'FAIL: {error}')
    if errors:
        print(f'FAIL: {len(errors)} repository issue(s)')
        return 1
    print(f'PASS: {len(paths)} tracked files; required layout, names, local file links, sensitive-file rules')
    print('Scope: inline Markdown file links only; no fragment/external URL check; not a complete secret scanner.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
