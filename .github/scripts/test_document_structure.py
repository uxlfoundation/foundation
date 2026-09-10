from pathlib import Path
import tempfile
import unittest
from check_document_structure import check


class StructureChecks(unittest.TestCase):
    def test_retired_destination_and_current_specification(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            page = root / 'README.md'
            page.write_text('[Spec](https://github.com/uxlfoundation/oneAPI-spec)\n', encoding='utf-8')
            self.assertTrue(any('retired specification' in e for e in check(root)))
            page.write_text('[Spec](https://uxlfoundation.org/specifications/oneapi/technical-overview/)\n', encoding='utf-8')
            self.assertEqual(check(root), [])

    def test_malformed_heading(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'README.rst').write_text('Long heading\n==========\n', encoding='utf-8')
            self.assertTrue(check(root))

    def test_wrong_existing_record_does_not_cover_omitted_record(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for date in ['2024-09-05', '2024-09-19']:
                (root / f'{date}.rst').write_text('Meeting\n=======\n', encoding='utf-8')
            index = root / 'README.rst'
            index.write_text('`September 5 <2024-09-05.rst>`__\n\n'
                             '`September 19 <2024-09-05.rst>`__\n', encoding='utf-8')
            self.assertTrue(any('2024-09-19.rst: missing' in e for e in check(root)))
            index.write_text('`September 5 <2024-09-05.rst>`__\n\n'
                             '`September 19 <2024-09-19.rst>`__\n', encoding='utf-8')
            self.assertEqual(check(root), [])


if __name__ == '__main__':
    unittest.main()
