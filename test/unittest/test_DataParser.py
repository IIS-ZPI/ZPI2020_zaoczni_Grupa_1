from unittest import TestCase

from app.DataParser import DataParser
from test.data_for_tests import invalid_test_data
from test.data_for_tests import valid_test_USD_data


class TestDataParser(TestCase):
    def test_parse_session_validDataset(self):

        actual_results = DataParser.parse_session(
            valid_test_USD_data["dataset"].copy())
        self.assertEqual(actual_results, valid_test_USD_data["results"])

    def test_parse_session_invalidDataset(self):

        actual_results = DataParser.parse_session(invalid_test_data["dataset"])
        self.assertEqual(actual_results, invalid_test_data["results"])
