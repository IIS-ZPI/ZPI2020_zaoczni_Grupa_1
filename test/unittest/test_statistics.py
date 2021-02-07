from unittest import TestCase

from app.DataParser import DataParser

from test.data_for_tests import valid_test_USD_data
from test.data_for_tests import invalid_test_data


class TestStatistics(TestCase):
    def test_parse_statistics_valid_data(self):
        actual_result = DataParser.parse_statistics(
            valid_test_USD_data["dataset"].copy())
        expected_result = {'median': 3.73, 'mode': 3.73,
                           'standard deviation value': 0.026, 'coeficient of Variation': 0.697}
        self.assertEqual(actual_result, expected_result)

    def test_parse_statistics_invalid_data(self):
        actual_result = DataParser.parse_statistics(
            invalid_test_data["dataset"].copy())
        self.assertIsNone(actual_result)
