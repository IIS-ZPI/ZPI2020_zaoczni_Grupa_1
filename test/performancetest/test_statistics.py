from unittest import TestCase

from time import perf_counter_ns

from app.DataParser import DataParser

from test.data_for_tests import valid_test_data
from test.data_for_tests import create_empty_file_in_directory


class TestStatistics(TestCase):
    threshold = 700000 #nanoseconds

    def __performance_run(self):
        session_data = valid_test_data["dataset"]

        t_start = perf_counter_ns()
        DataParser.parse_statistics(session_data)
        t_stop = perf_counter_ns()

        execution_time = t_stop - t_start
        return execution_time

    def test_parse_statistics_performance(self):
        file_path = create_empty_file_in_directory(
            "DataParser_get_statistics.txt", "test/performancetest/results"
        )
        if not file_path:
            self.fail(f"Couldn't create {file_path}")

        for i in range(1, 11):
            result = self.__performance_run()
            with open(file_path, "a") as res_file:
                res_file.write(f"Attempt: {i}\t|\tExecution time: {result}\n")
            self.assertTrue(result < TestStatistics.threshold)
