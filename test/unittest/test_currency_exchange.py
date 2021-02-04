from unittest import TestCase
from requests import get as get_request
from requests.exceptions import RequestException
from app.DataParser import DataParser


from test.data_for_tests import currency_EUR_exchange
from test.data_for_tests import currency_USD_exchange


class NBPRequestManagerMock:
    def get_ratio_changes(self, currency):

        json_address = f"http://api.nbp.pl/api/exchangerates/rates/a/{currency}/2020-12-31/2021-01-30/"
        try:
            response = get_request(json_address)
        except RequestException:
            print("Błąd pobierania danych")
            return None
        return response

    def show_ratio_changes(self, currency_one, currency_two):
        ratio_changes_data_one = self.get_ratio_changes(currency_one).json()
        ratio_changes_data_two = self.get_ratio_changes(currency_two).json()

        results = DataParser.parse_ratio_changes(
            ratio_changes_data_one, ratio_changes_data_two)
        return results


class TestCurrencyExchange(TestCase):
    def test_get_currency_data_USD(self):
        mock = NBPRequestManagerMock()
        actual_result_mock = mock.get_ratio_changes("USD").json()
        expected_result = currency_USD_exchange
        self.assertEqual(expected_result, actual_result_mock)

    def test_get_currency_data_EUR(self):
        mock = NBPRequestManagerMock()
        actual_result_mock = mock.get_ratio_changes("EUR").json()
        expected_result = currency_EUR_exchange
        self.assertEqual(expected_result, actual_result_mock)

    def test_get_currency_data_wrong_data(self):
        mock = NBPRequestManagerMock()
        try:
            actual_result_mock = mock.get_ratio_changes("WRONG").json()
        except:
            actual_result_mock = mock.get_ratio_changes("WRONG")
        expected_result = currency_EUR_exchange
        self.assertNotEqual(expected_result, actual_result_mock)

    def test_show_ratio_change_mock(self):
        mock = NBPRequestManagerMock()
        actual_result = mock.show_ratio_changes("USD", "EUR")
        expected_result = 1.3457
        self.assertEqual(expected_result, actual_result)

    def test_show_ratio_change_mock_wrong_result(self):
        mock = NBPRequestManagerMock()
        actual_result = mock.show_ratio_changes("EUR", "USD")
        expected_result = 1.3457
        self.assertNotEqual(expected_result, actual_result)

    def test_show_ratio_change_mock_wrong_currency(self):
        mock = NBPRequestManagerMock()
        try:
            actual_result = mock.show_ratio_changes("WRONG_CURRENCY", "USD")
        except:
            actual_result = None
        expected_result = 1.3457
        self.assertNotEqual(expected_result, actual_result)
