from unittest import TestCase

from time import perf_counter_ns

from requests import get as get_request
from requests.exceptions import RequestException
from app.DataParser import DataParser


from test.data_for_tests import create_empty_file_in_directory


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


class TestExchange(TestCase):
    threshold = 250000000  # nanoseconds

    def __performance_run(self):

        mock = NBPRequestManagerMock()

        t_start = perf_counter_ns()
        mock.show_ratio_changes("USD", "EUR")
        t_stop = perf_counter_ns()

        execution_time = t_stop - t_start
        return execution_time

    def test_show_ratio_changes_performance(self):
        file_path = create_empty_file_in_directory(
            "NBPRequestManager_show_ratio_changes.txt", "test/performancetest/results"
        )
        if not file_path:
            self.fail(f"Couldn't create {file_path}")

        for i in range(1, 11):
            result = self.__performance_run()
            with open(file_path, "a") as res_file:
                res_file.write(f"Attempt: {i}\t|\tExecution time: {result}\n")
            self.assertTrue(result < TestExchange.threshold)
