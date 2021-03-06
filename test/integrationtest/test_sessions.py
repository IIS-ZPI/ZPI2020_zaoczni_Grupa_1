from unittest import TestCase

from app.NBPRequestManager import NBPRequestManager
from app.DataParser import DataParser
from app.TimeframeType import TimeframeType


class TestSessionIntegration(TestCase):
    def test_session_request_parse_scenario(self):
        test_currency = "USD"
        test_timeframe = TimeframeType.WEEK

        session_data = NBPRequestManager.get_currency_data(
            test_currency, test_timeframe)
        results = DataParser.parse_session(session_data)
        results_regex = "{'increase': [0-9]+, 'decrease': [0-9]+, 'stable': [0-9]+}"

        self.assertRegex(str(results), results_regex)
