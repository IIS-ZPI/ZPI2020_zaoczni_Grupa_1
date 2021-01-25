from unittest import TestCase

from app.DataParser import DataParser

from test.data_for_tests import valid_test_data
from test.data_for_tests import invalid_test_data

class TestStatistics(TestCase):
    def test_parse_statistics_valid_data(self):
        actual_result = DataParser.parse_statistics(valid_test_data["dataset"])
        expected_result = {'median': 3.69, 'mode': 3.69, 'standard deviation value': 0.033, 'coeficient of Variation': 0.895}
        self.assertEqual(actual_result, expected_result)

    def test_parse_statistics_invalid_data(self):        
        actual_result = DataParser.parse_statistics(invalid_test_data["dataset"])
        self.assertIsNone(actual_result)
