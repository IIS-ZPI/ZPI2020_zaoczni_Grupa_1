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
        pass

    def parse_ratio_changes(ratio_changes_data):
        pass