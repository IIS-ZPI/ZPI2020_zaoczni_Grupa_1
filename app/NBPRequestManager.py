from datetime import date, timedelta
import requests

class NBPRequestManager:
    def get_sessions(currency, timeframe):

        yesterday = date.today()- timedelta(days=1)
        yesterday_format = yesterday.strftime("%Y-%m-%d")

        if(timeframe.name == 'WEEK'):
            startdate = date.today() - timedelta(days=7)
            startdate_format = startdate.strftime("%Y-%m-%d")
        elif(timeframe.name == 'TWO_WEEKS'):
            startdate = date.today() - timedelta(days=14)
            startdate_format = startdate.strftime("%Y-%m-%d")
        elif(timeframe.name == 'MONTH'):
            startdate = date.today() - timedelta(days=30)
            startdate_format = startdate.strftime("%Y-%m-%d")
        
        json_address = f"http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{startdate_format}/{yesterday_format}/"
        req_data = requests.get(json_address) #for parsing
        return req_data

    def get_statistics(currency, timeframe):
        #TODO
        pass

    def get_ratio_changes(currency_one, currency_two, timeframe):
        #TODO
        pass
