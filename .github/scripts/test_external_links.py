from urllib.error import HTTPError
from unittest import TestCase
from unittest.mock import patch
from report_external_links import eligible, probe


class ExternalLinkReportTests(TestCase):
    def test_restricted_response_is_not_reported_as_dead(self):
        with patch('report_external_links.urlopen', side_effect=HTTPError('https://example.org', 403, '', {}, None)):
            self.assertEqual(probe('https://example.org'), ('restricted or bot-blocked', '403'))

    def test_missing_response_is_reported(self):
        with patch('report_external_links.urlopen', side_effect=HTTPError('https://example.org', 404, '', {}, None)):
            self.assertEqual(probe('https://example.org'), ('missing', '404'))

    def test_private_recording_and_credential_links_are_excluded(self):
        for url in ['https://zoom.us/rec/share/abc', 'https://docs.google.com/document/d/abc',
                    'https://example.org/?token=secret', 'https://user:password@example.org/']:
            self.assertFalse(eligible(url))
        self.assertTrue(eligible('https://uxlfoundation.org/'))
