# Instrukcja Użytkownika

## Opis
OpenNBP Analyzer to aplikacja mający na celu umożliwienie użytkownikom dokonywania analiz danych walutowych dostępnych w serwisie NBP.

## Wymagania
- Python, w wersji 3.0 lub wyższej
- Moduł *requests* w wersji 2.25.1 lub wyższej
- Moduł *python-dateutil* w wersji 1.4 lub wyższej

Wszystkie niezbędne moduły można zainstalować jednocześnie poprzez instalację
managerem PIP (Pythonowy manager modułów) pliku *requirements.txt*,
dostarczanego wraz z aplikacją.

Przykład: *pip install -r 'requirements.txt'*

## Uruchomienie
Program jest uruchamiany poprzez plik skryptowy "run.py", znajdujący się w katalogu instalacyjnym aplikacji.

## Obsługa programu
- Aplikacja oferuje interfejs tekstowy (CLI).
- Użytkownik wprowadza w niej wartości znaczące np. USD.
- Komendy wybiera się poprzez wprowadzenie odpowiadającego numeru z listy.
- Polecenia w aplikacji zatwierdzane są klawiszem Enter.

## Funkcjonalności

### 1. Obliczanie sesji walutowych

#### Opis
Wyświetlanie informacji o przebiegu kolejnych sesji (wzrostowe, spadkowe, bez zmian) dla wybranej waluty.

#### Dane wejściowe
* Kod Waluty 
* Przedział Czasu 

#### Rezultaty
* Liczba sesji wzrostowych
* Liczba sesji spadkowych
* Liczba sesji bez zmian

#### Przykład użycia
1. Użytkownik wprowadza kod waluty "USD".
```
Podaj walutę (kod, np. USD): USD
```
2. Użytkownik wybiera numer odpowiadający przedziałowi czasowemu dwóch tygodni.
```
Podaj okres czasu: 2
```
3. Aplikacja wyświetla użytkownikowi wynik w postaci liczby dni kiedy występowała sesja wzrostowa, liczby dni ze spadkiem oraz liczbę dni bez żadnych zmian.
```
Wynik: 
Dni wzrostu: 4
Dni spadkowe: 5
Dni bez zmian: 0
```

### 2. Obliczanie miar statystycznych

#### Opis
Wyświetlanie informacji o medianie, dominancie, odchyleniu standardowym oraz o współczynniku zmienności dla wybranej przez użytkownika waluty.

#### Dane wejściowe
* Kod Waluty 
* Przedział Czasu 

#### Rezultaty
* Mediana wyników
* Dominanta wyników
* Odchylenie standardowe zbioru
* Współczynnik zmienności zbioru

#### Przykład użycia
1. Użytkownik wprowadza kod waluty GBP i numer odpowiadający przedziałowi czasowemu dla którego interesują go statystyka (3 - miesiąc).

2. Aplikacja wyświetla użytkownikowi Medianę, dominantę, odchylenie standardowe oraz współczynnik zmienności dla Funta Brytyjskiego z okresu 3 miesięcy:
```
Mediana wyników: 5.12
Dominanta wyników:5.12
Odchylenie standardowe zbioru : 0.018
Współczynnik zmienności zbioru : 0.352
```

### 3. Rozkład zmian pomiędzy dwoma walutami

#### Opis
Wyświetlanie procentowego stosunku zmiany kursów dwóch wybranych przez użytkownika walut w wybranym przez niego okresie czasu.

#### Dane wejściowe
* Kod pierwszej waluty 
* Kod drugiej waluty 
* Przedział Czasu 

#### Rezultaty
* Procentowy stosunek zmiany kursu jednej waluty względem drugiej

#### Przykłady Użycia
1. Użytkownik wprowadza kod pierwszej waluty - GBP.

2. Później kod drugiej waluty - USD.
```
Podaj drugą walutę (kod, np. USD):USD
```
3. Wpisuje liczbę odpowiadającą kwartałowi - 2.

4. Aplikacja wyświetla użytkownikowi wynik w postaci procentowego stosunku zmiany jednej waluty do drugiej.
```
Zmiana kursu GBP względem USD: 5.1279%
```

### Wyjście z programu.
Użytkownik wychodzi z programu wybierając odpowiednią komendę z listy w menu aplikacji. 