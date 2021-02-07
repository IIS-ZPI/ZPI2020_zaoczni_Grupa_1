from unittest import TestCase
from requests import get as get_request
from requests.exceptions import RequestException
from app.DataParser import DataParser


from test.data_for_tests import valid_test_USD_data
from test.data_for_tests import valid_test_EUR_data
from test.data_for_tests import invalid_test_data


class TestCurrencyExchange(TestCase):
    def test_get_currency_data_EUR_USD(self):

        session_data_EUR = valid_test_EUR_data["dataset"].copy()
        session_data_USD = valid_test_USD_data["dataset"].copy()
        actual_result = DataParser.parse_ratio_changes(
            session_data_EUR, session_data_USD)
        expected_result = -1.3278
        self.assertEqual(expected_result, actual_result)

    def test_get_currency_data_USD_EUR(self):

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

    def test_get_currency_data_wrong_data(self):
        session_data_EUR = valid_test_EUR_data["dataset"].copy()

        actual_result = DataParser.parse_ratio_changes(
            invalid_test_data.copy(), session_data_EUR)

        expected_result = None
        self.assertEqual(expected_result, actual_result)
