from unittest import TestCase

from app.NBPRequestManager import NBPRequestManager
from app.DataParser import DataParser
from app.TimeframeType import TimeframeType


class TestStatisticsIntegration(TestCase):
    def test_statistics_request_parse_scenario(self):
        test_currency = "USD"
        test_timeframe = TimeframeType.WEEK

        statistics_data = NBPRequestManager.get_currency_data(
            test_currency, test_timeframe)

        results = DataParser.parse_statistics(statistics_data)
        results_regex = "{'median': [0-9]+.?[0-9]+, 'mode': [0-9]+.?[0-9]+, " + \
                        "'standard deviation value': [0-9]+.?[0-9]+, " + \
                        "'coeficient of Variation': [0-9]+.?[0-9]+}"

        self.assertRegex(str(results), results_regex)
