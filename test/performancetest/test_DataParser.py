from unittest import TestCase

from time import perf_counter_ns

from app.DataParser import DataParser

class TestDataParser(TestCase):
    threshold = 4000 #nanoseconds

    session_data_header = {
        'code': 'USD',
        'currency': 'dolar amerykański',
        'table': 'A'
    } 

    session_data_rates = {
        'rates': [
            {'effectiveDate': '2020-12-17', 'mid': 3.6254, 'no': '246/A/NBP/2020'}, 
            {'effectiveDate': '2020-12-18', 'mid': 3.6322, 'no': '247/A/NBP/2020'}, 
            {'effectiveDate': '2020-12-21', 'mid': 3.7082, 'no': '248/A/NBP/2020'}, 
            {'effectiveDate': '2020-12-22', 'mid': 3.6921, 'no': '249/A/NBP/2020'}, 
            {'effectiveDate': '2020-12-23', 'mid': 3.6919, 'no': '250/A/NBP/2020'}, 
            {'effectiveDate': '2020-12-24', 'mid': 3.6981, 'no': '251/A/NBP/2020'}, 
            {'effectiveDate': '2020-12-28', 'mid': 3.6639, 'no': '252/A/NBP/2020'}, 
            {'effectiveDate': '2020-12-29', 'mid': 3.6778, 'no': '253/A/NBP/2020'}, 
            {'effectiveDate': '2020-12-30', 'mid': 3.6901, 'no': '254/A/NBP/2020'}, 
            {'effectiveDate': '2020-12-31', 'mid': 3.7584, 'no': '255/A/NBP/2020'}, 
            {'effectiveDate': '2021-01-04', 'mid': 3.6998, 'no': '001/A/NBP/2021'}, 
            {'effectiveDate': '2021-01-05', 'mid': 3.7031, 'no': '002/A/NBP/2021'}, 
            {'effectiveDate': '2021-01-07', 'mid': 3.6656, 'no': '003/A/NBP/2021'}, 
            {'effectiveDate': '2021-01-08', 'mid': 3.6919, 'no': '004/A/NBP/2021'}
        ] 
    }

    def __performance_run(self, amount_of_days):
        session_data = TestDataParser.session_data_header
        session_data["rates"] = TestDataParser.session_data_rates["rates"][:amount_of_days]

        t_start = perf_counter_ns()
        DataParser.parse_session(session_data)
        t_stop = perf_counter_ns() 

        execution_time = t_stop - t_start
        return execution_time

    def test_parse_session_performance(self):
        cycles_test_amount_of_days = [1, 7, 14]
        print("")
        for amount_of_days in cycles_test_amount_of_days:
            result = self.__performance_run(amount_of_days)
            print(f"Number of days: {amount_of_days} | Execution time: {result}")
            self.assertTrue(result < amount_of_days * TestDataParser.threshold)