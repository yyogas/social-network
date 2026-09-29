#!/usr/bin/env python3
"""Check the event's explicit Git delta, not the synthetic merge commit diff."""
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ZERO = '0' * 40


def git(*args: str) -> str:
    return subprocess.check_output(['git', *args], text=True, stderr=subprocess.PIPE).strip()


def commit(value: str) -> str:
    if not isinstance(value, str) or not re.fullmatch(r'[0-9a-f]{40}', value):
        raise ValueError('Expected a full commit SHA')
    git('cat-file', '-e', value + '^{commit}')
    return value


def endpoints(event_name: str, event: dict) -> tuple[str, str]:
    if event_name == 'pull_request':
        base = commit(event['pull_request']['base']['sha'])
        head = commit(event['pull_request']['head']['sha'])
        return git('merge-base', base, head), head
    if event_name == 'push':
        head = commit(event['after'])
        before = event['before']
        if before == ZERO:
            empty = subprocess.check_output(['git', 'hash-object', '-t', 'tree', '--stdin'],
                                            input='', text=True).strip()
            return empty, head
        return commit(before), head
    raise ValueError('Unsupported event; no whitespace check performed')


def main() -> int:
    try:
        event = json.loads(Path(os.environ['GITHUB_EVENT_PATH']).read_text())
        base, head = endpoints(os.environ['GITHUB_EVENT_NAME'], event)
        print(f'Whitespace range: {base}..{head}', flush=True)
        return subprocess.run(['git', '-c', 'core.whitespace=blank-at-eol,blank-at-eof,space-before-tab',
                               'diff', '--check', base, head, '--'], check=False).returncode
    except (KeyError, ValueError, TypeError, OSError, subprocess.CalledProcessError) as error:
        print(f'FAIL: cannot resolve whitespace range ({type(error).__name__})', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
