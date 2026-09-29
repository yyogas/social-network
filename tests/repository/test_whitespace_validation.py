"""Exercise real Git histories, including GitHub's synthetic merge topology."""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[2] / 'scripts/repository/check_whitespace.py'


class WhitespaceValidationTests(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.root = Path(self.folder.name)
        self.git('init', '-b', 'main')
        self.git('config', 'user.email', 'tests@example.invalid')
        self.git('config', 'user.name', 'Synthetic Test')
        self.base = self.save('README.md', '# Base\n')

    def git(self, *args):
        return subprocess.check_output(['git', *args], cwd=self.root, text=True,
                                       stderr=subprocess.PIPE).strip()

    def save(self, filename, contents):
        (self.root / filename).write_text(contents)
        self.git('add', filename)
        self.git('commit', '-m', 'Synthetic fixture')
        return self.git('rev-parse', 'HEAD')

    def check(self, name, event):
        path = self.root / 'event.json'
        path.write_text(json.dumps(event))
        env = dict(os.environ, GITHUB_EVENT_NAME=name, GITHUB_EVENT_PATH=str(path))
        return subprocess.run(['python3', str(SCRIPT)], cwd=self.root, env=env,
                              capture_output=True, text=True).returncode

    def pr(self, base, head):
        return self.check('pull_request', {'pull_request': {'base': {'sha': base},
                                                         'head': {'sha': head}}})

    def merge_fixture(self, dirty):
        self.git('checkout', '-b', 'candidate')
        head = self.save('candidate.md', 'candidate  \n' if dirty else 'candidate\n')
        self.git('checkout', 'main')
        base = self.save('unrelated.md', 'base change\n')
        self.git('merge', '--no-ff', 'candidate', '-m', 'Synthetic PR merge')
        return base, head

    def test_dirty_pr_on_synthetic_merge_fails_when_old_check_passes(self):
        base, head = self.merge_fixture(True)
        old = subprocess.run(['git', 'show', '--format=', '--check', 'HEAD'],
                             cwd=self.root, capture_output=True)
        self.assertEqual(0, old.returncode, 'Must reproduce the original blind spot')
        self.assertEqual(2, self.pr(base, head))

    def test_clean_pr_on_synthetic_merge_passes(self):
        base, head = self.merge_fixture(False)
        self.assertEqual(0, self.pr(base, head))

    def test_pr_excludes_unrelated_base_changes(self):
        self.git('checkout', '-b', 'candidate')
        head = self.save('candidate.md', 'clean\n')
        self.git('checkout', 'main')
        base = self.save('unrelated.md', 'bad base  \n')
        self.assertEqual(0, self.pr(base, head))

    def test_push_checks_entire_delta_not_last_commit(self):
        self.save('first.md', 'bad  \n')
        head = self.save('last.md', 'clean\n')
        self.assertEqual(2, self.check('push', {'before': self.base, 'after': head}))

    def test_clean_push_passes(self):
        head = self.save('clean.md', 'clean\n')
        self.assertEqual(0, self.check('push', {'before': self.base, 'after': head}))

    def test_first_push_checks_against_empty_tree(self):
        head = self.save('first.md', 'bad  \n')
        self.assertEqual(2, self.check('push', {'before': '0' * 40, 'after': head}))

    def test_missing_commit_fails_closed(self):
        self.assertEqual(1, self.pr('f' * 40, self.base))

    def test_invalid_commit_and_unsupported_event_fail_closed(self):
        self.assertEqual(1, self.pr('--help', self.base))
        self.assertEqual(1, self.check('workflow_dispatch', {}))


if __name__ == '__main__':
    unittest.main()
