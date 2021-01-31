from app.NBPRequestManager import NBPRequestManager
from app.DataParser import DataParser
import json

class DataPresenter:
    def show_sessions(currency, timeframe):
        session_data = NBPRequestManager.get_sessions(currency, timeframe).json()
        results = DataParser.parse_session(session_data)
        
        if results:
            print(f"Dni wzrostu: {results['increase']}\nDni spadkowe: {results['decrease']}\nDni bez zmian: {results['stable']}\n")         
        
    def show_statistics(currency, timeframe):
        statistics_data = NBPRequestManager.get_statistics(currency, timeframe).json()
        results = DataParser.parse_statistics(statistics_data)

        if results:
            print(f"Mediana wyników: {results['median']}")
            print(f"Dominanta wyników:{results['mode']}")
            print(f"Odchylenie standardowe zbioru : {results['standard deviation value']}")
            print(f"Współczynnik zmienności zbioru : {results['coeficient of Variation']}")

    def show_ratio_changes(currency_one, currency_two, timeframe):
        ratio_changes_data_one = NBPRequestManager.get_ratio_changes(currency_one, timeframe).json()
        ratio_changes_data_two = NBPRequestManager.get_ratio_changes(currency_two, timeframe).json()
        
        results = DataParser.parse_ratio_changes(ratio_changes_data_one, ratio_changes_data_two)

        if results:
            if results['first change'] > 0:
                print(f"Wartość kursu pierwszej waluty po wybranym okresie : +{results['first change']}%")
            else:
                print(f"Wartość kursu pierwszej waluty po wybranym okresie : {results['first change']}%")
            
            if results['second change'] > 0:
                print(f"Wartość kursu drugiej waluty po wybranym okresie : +{results['second change']}%")
            else:
                print(f"Wartość kursu drugiej waluty po wybranym okresie : {results['second change']}%")
            
            print(f"Stosunek pierwszej waluty do drugiej waluty : {results['compare change']}%")
        
