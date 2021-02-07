from unittest import TestCase

from time import perf_counter_ns

from app.DataParser import DataParser
from test.data_for_tests import valid_test_USD_data
from test.utility_functions import create_empty_file_in_directory


class TestSessionDataParser(TestCase):
    threshold = 2000  # nanoseconds

    def __performance_run(self, amount_of_days, method):
        session_data = valid_test_USD_data["dataset"].copy()
        session_data["rates"] = session_data["rates"][:amount_of_days]

        t_start = perf_counter_ns()
        method(session_data)
        t_stop = perf_counter_ns()

        execution_time = t_stop - t_start
        return execution_time

    def test_parse_session_performance(self):
        file_path = create_empty_file_in_directory(
            "DataParser_get_session.txt", "test/performancetest/results")
        if not file_path:
            self.fail(f"Couldn't create {file_path}")

        for amount_of_days in range(1, len(valid_test_USD_data["dataset"]['rates'])+1):
            result = self.__performance_run(
                amount_of_days, DataParser.parse_session)
            with open(file_path, "a") as res_file:
                res_file.write(
                    f"Number of days: {amount_of_days} | Execution time: {result}\n")

            self.assertTrue(
                result < amount_of_days * TestSessionDataParser.threshold * 5
                if amount_of_days == 1
                else result < amount_of_days * TestSessionDataParser.threshold
            )
