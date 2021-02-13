from app.NBPRequestManager import NBPRequestManager
from app.DataParser import DataParser


class DataPresenter:
    def show_sessions(currency, timeframe):
        session_data = NBPRequestManager.get_sessions(currency, timeframe).json()
        results = DataParser.parse_session(session_data)

        if results:
            return ('Dni wzrostu: {}\n' +
                    'Dni spadkowe: {}\n' +
                    'Dni bez zmian: {}').format(results['increase'], results['decrease'], results['stable'])

    def show_statistics(currency, timeframe):
        statistics_data = NBPRequestManager.get_statistics(currency, timeframe).json()
        results = DataParser.parse_statistics(statistics_data)

        if results:
            results_presentation = ""
            results_presentation += f"Mediana wyników: {results['median']}\n"
            results_presentation += f"Mediana wyników: {results['median']}\n"
            results_presentation += f"Dominanta wyników:{results['mode']}\n"
            results_presentation += f"Odchylenie standardowe zbioru : {results['standard deviation value']}\n"
            results_presentation += f"Współczynnik zmienności zbioru : {results['coeficient of Variation']}"
            return results_presentation

    def show_ratio_changes(currency_one, currency_two, timeframe):
        ratio_changes_data_one = NBPRequestManager.get_ratio_changes(currency_one, timeframe).json()
        ratio_changes_data_two = NBPRequestManager.get_ratio_changes(currency_two, timeframe).json()

        results = DataParser.parse_ratio_changes(ratio_changes_data_one, ratio_changes_data_two)

        if results:
            return f"Zmiana kursu {currency_one} względem {currency_two}: {results}%"
