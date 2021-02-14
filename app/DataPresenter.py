from app.NBPRequestManager import NBPRequestManager
from app.DataParser import DataParser


class DataPresenter:
    def show_sessions(currency, timeframe):
        session_data = NBPRequestManager.get_currency_data(currency, timeframe)
        results = DataParser.parse_session(session_data)

        if results:
            return (f"Dni wzrostu: {results['increase']}\n" +
                    f"Dni spadkowe: {results['decrease']}\n" +
                    f"Dni bez zmian: {results['stable']}")

    def show_statistics(currency, timeframe):
        statistics_data = NBPRequestManager.get_currency_data(currency, timeframe)
        results = DataParser.parse_statistics(statistics_data)

        if results:
            results_presentation = ""
            results_presentation += f"Mediana wyników: {results['median']}\n"
            results_presentation += f"Mediana wyników: {results['median']}\n"
            results_presentation += f"Dominanta wyników: {results['mode']}\n"
            results_presentation += f"Odchylenie standardowe zbioru: {results['standard deviation value']}\n"
            results_presentation += f"Współczynnik zmienności zbioru: {results['coeficient of Variation']}"
            return results_presentation

    def show_ratio_changes(currency_one, currency_two, timeframe):
        ratio_changes_data_one = NBPRequestManager.get_currency_data(currency_one, timeframe)
        ratio_changes_data_two = NBPRequestManager.get_currency_data(currency_two, timeframe)

        results = DataParser.parse_ratio_changes(ratio_changes_data_one, ratio_changes_data_two)

        if results:
            return f"Zmiana kursu {currency_one} względem {currency_two}: {results}%"
