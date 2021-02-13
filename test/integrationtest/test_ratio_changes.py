from unittest import TestCase

from app.NBPRequestManager import NBPRequestManager
from app.DataParser import DataParser
from app.TimeframeType import TimeframeType


class TestRatioChangesIntegration(TestCase):
    def test_ratio_changes_request_parse_scenario(self):
        test_currency_one = "USD"
        test_currency_two = "EUR"
        test_timeframe = TimeframeType.WEEK

        ratio_changes_data_one = NBPRequestManager.get_ratio_changes(
            test_currency_one, test_timeframe).json()
        ratio_changes_data_two = NBPRequestManager.get_ratio_changes(
            test_currency_two, test_timeframe).json()

        results = DataParser.parse_ratio_changes(
            ratio_changes_data_one, ratio_changes_data_two)
        results_regex = "-?[0-9]+.[0-9]+"

        self.assertRegex(str(results), results_regex)
