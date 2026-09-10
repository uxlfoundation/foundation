from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from report_new_attachments import large_additions, LIMIT


class AttachmentTests(unittest.TestCase):
    def test_added_only_and_size_boundary(self):
        with patch('report_new_attachments.subprocess.check_output', side_effect=[
            'at limit.pdf\0large file.pdf\0', str(LIMIT), str(LIMIT + 1)
        ]) as run:
            self.assertEqual(large_additions('base', 'head'), [('large file.pdf', LIMIT + 1)])
            self.assertIn('--diff-filter=A', run.call_args_list[0].args[0])
            self.assertIn('-M', run.call_args_list[0].args[0])

    def test_existing_and_renamed_assets_are_excluded(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            def git(*args):
                return subprocess.check_output(['git', '-C', directory, *args], text=True).strip()
            git('init', '-q')
            git('config', 'user.name', 'Fixture')
            git('config', 'user.email', 'fixture@example.org')
            (root / 'old.pdf').write_bytes(b'x' * (LIMIT + 1))
            git('add', '.')
            git('commit', '-qm', 'base')
            base = git('rev-parse', 'HEAD')
            git('mv', 'old.pdf', 'renamed.pdf')
            (root / 'new.pdf').write_bytes(b'y' * (LIMIT + 1))
            git('add', '.')
            git('commit', '-qm', 'new attachment and rename')
            import os
            previous = os.getcwd()
            try:
                os.chdir(directory)
                self.assertEqual(large_additions(base), [('new.pdf', LIMIT + 1)])
            finally:
                os.chdir(previous)
