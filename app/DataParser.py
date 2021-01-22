import statistics

class DataParser:
    def parse_session(session_data):
        if not session_data:
            return None
        
        last_mid = None
        increase = 0
        decrease = 0
        stable = 0
        try:
            for element in session_data['rates']:
                current_mid = element.get("mid")
                if last_mid is None:
                    last_mid = current_mid
                    continue
                else:
                    if current_mid > last_mid:
                        increase+=1
                    elif current_mid < last_mid:
                        decrease+=1
                    else:
                        stable+=1
                last_mid = current_mid 
        except:
            print("Błąd parsowania danych")
            return None
        
        return {"increase": increase, "decrease": decrease, "stable": stable}
    
    def parse_statistics(statistics_data):
        if not statistics_data:
            return None

        values = []

        try:
            for element in statistics_data['rates']:
                values.append(element.get("mid"))  
        except:
            print("Błąd parsowania danych")
            return None
        

        rounded_values_list = [round(x,2) for x in values] #rounding values to 2 elements after coma
        rounded_values_list.sort() #sorting in ascending order (for median value)

        mean = sum(rounded_values_list)/len(rounded_values_list)

        median_value = statistics.median(rounded_values_list)
        mode_value = statistics.mode(rounded_values_list)
        std_dev_value = round(statistics.stdev(rounded_values_list), 3)
        coef_var = round((std_dev_value/mean)*100, 3)
  
        return {"median": median_value , "mode": mode_value, "standard deviation value": std_dev_value, "coeficient of Variation": coef_var}        


    def parse_ratio_changes(ratio_changes_data):
        pass