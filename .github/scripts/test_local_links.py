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
                'Agenda\n======\n\n'
                '.. _slides: ../slides%20with%20spaces.pdf\n'
                '`slides <../slides with spaces.pdf>`__\n'
                '.. _site: https://example.org/missing\n', encoding='utf-8')
            (root / 'README.md').write_text(
                '# Agenda\n'
                '[multi\nline](docs/notes.rst#agenda)\n'
                '[slides](<slides with spaces.pdf>)\n'
                '[root](/docs/notes.rst)\n'
                '[anchor](#agenda)\n[mail](mailto:test@example.org)\n', encoding='utf-8')
            self.assertEqual(check(root), [])

    def test_section_ids_and_missing_fragment(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'README.md').write_text(
                '# Café &amp; `code`\n# Repeat\n# Repeat\n'
                '[unicode](#caf%C3%A9--code)\n[repeat](#repeat-1)\n'
                '[explicit](notes.rst#custom)\n[bad](notes.rst#missing)\n'
                '[pdf](slides.pdf#page=2)\n'
                '```markdown\n# Repeat\n```\n# Repeat\n[third](#repeat-2)\n', encoding='utf-8')
            (root / 'notes.rst').write_text('.. _custom:\n\nAgenda\n======\n', encoding='utf-8')
            (root / 'slides.pdf').touch()
            errors = check(root)
            self.assertEqual(len(errors), 1)
            self.assertIn('missing section: notes.rst#missing', errors[0])

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
