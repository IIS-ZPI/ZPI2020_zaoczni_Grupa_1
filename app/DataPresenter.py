from app.NBPRequestManager import NBPRequestManager
import json

class DataPresenter:
    def show_sessions(currency, timeframe):
        session_data = NBPRequestManager.get_sessions(currency, timeframe) #req_data
        answer = session_data.json()
       
        last_mid = None
        wzrostowe = 0
        spadkowe = 0
        bez_zmian = 0
        for element in answer['rates']:
            temp = element.get("mid")
            if last_mid is None:
                last_mid = temp
                continue
            else:
                if temp > last_mid:
                    wzrostowe+=1
                elif temp < last_mid:
                    spadkowe+=1
                else:
                    bez_zmian+=1
            last_mid = temp 

        print("dni wzrostu: " + str(wzrostowe) + ", dni spadkowe: " + str(spadkowe) + ", bez zmian: " + str(bez_zmian))
        

    def show_statistics(currency, timeframe):
        statistics_data = NBPRequestManager.get_statistics(currency, timeframe)
        #TODO: Parse and present

    def show_ratio_changes(currency_one, currency_two, timeframe):
        ratio_changes_data = NBPRequestManager.get_ratio_changes(currency_one, currency_two, timeframe)
        #TODO: Parse and present
