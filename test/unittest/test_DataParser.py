from unittest import TestCase

from app.DataParser import DataParser
from test.data_for_tests import invalid_test_data
from test.data_for_tests import valid_test_USD_data
from test.data_for_tests import valid_test_EUR_data


class TestDataParser(TestCase):
    def test_parse_session_validDataset(self):
        actual_results = DataParser.parse_session(
            valid_test_USD_data["dataset"].copy())

        self.assertEqual(actual_results, valid_test_USD_data["results"])

    def test_parse_session_invalidDataset(self):
        actual_results = DataParser.parse_session(invalid_test_data["dataset"])

        self.assertEqual(actual_results, invalid_test_data["results"])

    def test_parse_statistics_USD_valid_data(self):
        actual_result = DataParser.parse_statistics(
            valid_test_USD_data["dataset"].copy())
        expected_result = {'median': 3.73, 'mode': 3.73,
                           'standard deviation value': 0.026, 'coeficient of Variation': 0.697}

        self.assertEqual(actual_result, expected_result)

    def test_parse_statistics_invalid_data(self):
        actual_result = DataParser.parse_statistics(
            invalid_test_data["dataset"].copy())

        self.assertIsNone(actual_result)

    def test_get_currency_data_EUR_USD_valid(self):
        session_data_EUR = valid_test_EUR_data["dataset"].copy()
        session_data_USD = valid_test_USD_data["dataset"].copy()
        actual_result = DataParser.parse_ratio_changes(
            session_data_EUR, session_data_USD)
        expected_result = -1.3278

        self.assertEqual(expected_result, actual_result)

    def test_get_currency_data_USD_EUR_valid(self):
        session_data_EUR = valid_test_EUR_data["dataset"].copy()
        session_data_USD = valid_test_USD_data["dataset"].copy()
        actual_result = DataParser.parse_ratio_changes(
            session_data_USD, session_data_EUR)
        expected_result = 1.3457

        self.assertEqual(expected_result, actual_result)

    def test_get_currency_data_USD_invalid_data(self):
        session_data_USD = valid_test_USD_data["dataset"].copy()
        actual_result = DataParser.parse_ratio_changes(
            session_data_USD, invalid_test_data.copy())
        expected_result = None

        self.assertEqual(expected_result, actual_result)

    def test_get_currency_data_invalid_data_EUR(self):
        session_data_EUR = valid_test_EUR_data["dataset"].copy()
        actual_result = DataParser.parse_ratio_changes(
            invalid_test_data.copy(), session_data_EUR)
        expected_result = None

        self.assertEqual(expected_result, actual_result)
