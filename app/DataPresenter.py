from app.NBPRequestManager import NBPRequestManager

class DataPresenter:
    def show_sessions(currency, timeframe):
        session_data = NBPRequestManager.get_sessions(currency, timeframe)
        #TODO: Parse and present

    def show_statistics(currency, timeframe):
        statistics_data = NBPRequestManager.get_statistics(currency, timeframe)
        #TODO: Parse and present

    def show_ratio_changes(currency_one, currency_two, timeframe):
        ratio_changes_data = NBPRequestManager.get_ratio_changes(currency_one, currency_two, timeframe)
        #TODO: Parse and present
