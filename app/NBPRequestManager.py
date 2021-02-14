from requests import get as get_request
from requests.exceptions import RequestException
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from app.TimeframeType import TimeframeType


class NBPRequestManager:
    timedeltasList = {
            TimeframeType.WEEK: relativedelta(weeks=+1),
            TimeframeType.TWO_WEEKS: relativedelta(weeks=+2),
            TimeframeType.MONTH: relativedelta(months=+1),
            TimeframeType.QUARTER: relativedelta(months=+3),
            TimeframeType.YEAR: relativedelta(years=+1)
    }

    def get_currency_data(currency, timeframe):

        yesterday = date.today() - timedelta(days=1)  # starting since yesterday
        startdate = yesterday - NBPRequestManager.timedeltasList[timeframe]
        print(f"Start: {startdate} | End: {yesterday}")

        json_address = f"http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{startdate}/{yesterday}/"
        try:
            response = get_request(json_address).json()
        except RequestException:
            print("Błąd pobierania danych")
            return None
        return response
