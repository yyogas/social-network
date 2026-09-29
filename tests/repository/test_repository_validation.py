"""Regression cases: broken links and sensitive files must fail the gate."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[2] / 'scripts/repository/validate_repository.py'
SPEC = importlib.util.spec_from_file_location('repository_validator', SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class RepositoryValidationTests(unittest.TestCase):
    def check_files(self, files):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for name, content in files.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content)
            return MODULE.inspect(root, list(files), require_layout=False)

    def test_valid_local_link_and_standard_names(self):
        self.assertEqual([], self.check_files({'README.md': '[Guide](documentation/guide.md)',
                                              'documentation/guide.md': '# Guide'}))

    def test_broken_link_is_rejected(self):
        self.assertTrue(any('Broken local link' in e for e in self.check_files({'README.md': '[Missing](absent.md)'})))

    def test_external_link_does_not_need_network(self):
        self.assertEqual([], self.check_files({'README.md': '[Website](https://example.com/path)'}))

    def test_fenced_example_is_not_a_link_requirement(self):
        self.assertEqual([], self.check_files({'README.md': '```md\n[Example](absent.md)\n```\n'}))

    def test_environment_file_is_rejected(self):
        self.assertTrue(any('Forbidden tracked file' in e for e in self.check_files({'.env': 'SAMPLE=synthetic'})))

    def test_environment_example_is_allowed(self):
        self.assertEqual([], self.check_files({'configuration/.env.example': '# No real secrets'}))

    def test_private_key_marker_is_rejected_without_disclosing_value(self):
        marker = '-----BEGIN ' + 'PRIVATE KEY-----'
        errors = self.check_files({'README.md': marker})
        self.assertTrue(any('Private-key marker' in e for e in errors))
        self.assertFalse(any(marker in e for e in errors))

    def test_link_escape_is_rejected(self):
        self.assertTrue(any('Link escapes' in e for e in self.check_files({'README.md': '[Outside](../../outside.md)'})))

    def test_ambiguous_name_is_rejected(self):
        self.assertTrue(any('Ambiguous name' in e for e in self.check_files({'documentation/final2.md': '# Draft'})))

    def test_existing_untracked_file_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'README.md').write_text('[Draft](draft.md)')
            (root / 'draft.md').write_text('# Untracked')
            errors = MODULE.inspect(root, ['README.md'], require_layout=False)
            self.assertTrue(any('not tracked' in e for e in errors))

    def test_directory_link_requires_tracked_descendant(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'README.md').write_text('[Docs](documentation/)')
            (root / 'documentation').mkdir()
            (root / 'documentation' / 'guide.md').write_text('# Guide')
            errors = MODULE.inspect(root, ['README.md'], require_layout=False)
            self.assertTrue(any('no tracked content' in e for e in errors))
            self.assertEqual([], MODULE.inspect(root, ['README.md', 'documentation/guide.md'],
                                                require_layout=False))

    def test_missing_layout_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertTrue(any('Missing required file' in e for e in MODULE.inspect(Path(folder), [])))


if __name__ == '__main__':
    unittest.main()
