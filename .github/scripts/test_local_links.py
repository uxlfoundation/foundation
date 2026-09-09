from pathlib import Path
import tempfile
import unittest
from check_local_links import check


class LocalLinkTests(unittest.TestCase):
    def test_local_targets_and_external_links(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'docs').mkdir()
            (root / 'slides with spaces.pdf').touch()
            (root / 'docs' / 'notes.rst').write_text(
                '.. _slides: ../slides%20with%20spaces.pdf\n'
                '`slides <../slides with spaces.pdf>`__\n'
                '.. _site: https://example.org/missing\n', encoding='utf-8')
            (root / 'README.md').write_text(
                '[multi\nline](docs/notes.rst#agenda)\n'
                '[slides](<slides with spaces.pdf>)\n'
                '[root](/docs/notes.rst)\n'
                '[anchor](#agenda)\n[mail](mailto:test@example.org)\n', encoding='utf-8')
            self.assertEqual(check(root), [])

    def test_missing_case_mismatch_and_escape(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'note.rst').touch()
            (root / 'README.md').write_text(
                '[missing](missing.pdf)\n[case](NOTE.rst)\n'
                '[outside](../outside.md)\n[reference]: missing.rst\n', encoding='utf-8')
            self.assertEqual(len(check(root)), 4)


if __name__ == '__main__':
    unittest.main()
