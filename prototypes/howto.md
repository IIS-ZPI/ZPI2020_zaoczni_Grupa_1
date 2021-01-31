# NBP API
*Dokumentacja*
###### **Źródła**
[Dokumentacja NBP](http://api.nbp.pl/)
[Requests Library](https://requests.readthedocs.io/en/master/)

#### Podstawowe Informacje o API:
Dokumentacja udostępniona przez NBP jest **wystarczająco treściwa oraz przystępna**. Zawiera liczne przykłady. Opiszę w takim razie tylko sposób korzystania z biblioteki **Requests**, która ułatwia korzystanie z API. 
API samo w sobie pozwala na definiowanie z jakiego okresu potrzebujemy danych, z jakiej tabeli, czego te dane mają dotyczyć (waluta), oraz **czy mają być zwrócone jako XML lub JSON.** Ostatni parametr nie musi być przez nas definiowany, bo w łatwiejszy sposób interpretacji umożliwia nam poniższa biblioteka. 
#### Requsts
Dzięki bibliotece requests, możemy wysyłać zapytania do strony. Odpowiedź strony możemy w różny sposób interpretować. **Kilka przykładów**.
```
r = requests.get(address)
print(r.json())
```
W powyższym przykładzie widzimy odpowiedź na dany adres czyli np. http://api.nbp.pl/api/exchangerates/rates/a/chf/
ma zwrócić nam w konsoli jsonową zawartość. 

```
r = requests.get(address)
print(r.text)
```
W konsoli wyświetli nam się odpowedź w pełnej wersji tekstowej. Dla podanego adresu jest to domyślnie JSON. 
```
r = requests.get(address)
print(r.status_code)
```
Powyższy przykład zwróci nam odpowiedź liczbową serwera. 200, 300, 400 lub 500. Pamiętajmy, że jeżeli nie ma pewnych danych, bo tabela nie została jeszcze przez Narodowy bank opublikowana, to dostaniemy odpowedź **404**. Szczegóły - na stronie NBP.
```
r = requests.get(address)
print(r.url)
```
Zwrócony zotanie nam adres, który podaliśmy na wejściu.

Ponadto biblioteka ta umożliwia nam korzystanie z innych zapytań niż get, lecz na dobrą sprawę do projektu będziemy potrzebować tylko pobierania danych z archiwum Narodowego Banku Polskiego.

**Rozwinięcie tematu** dostępne w tym [filmiku](https://youtu.be/tb8gHvYlCFs), oraz w linku do dokumentacji **Requests**.
### Skrypt:
Podstawowy skrypt proszący od użytkownika o adres, zgodny z wytycznymi dostępnymi w dokumentacji NBP API, oraz wyświetlający w konsoli odpowiedź jako json, oraz zapisujący JSON-a do pliku tekstowego. Korzysta z prostego pobrania adresu od użytkownika **(można skorzystać z przykładów na stronie NBP)** oraz z tradycyjnego sposobu zapisu otwierającego plik. Kod dostępny w repozytorium pod nazwą **app.py**.
