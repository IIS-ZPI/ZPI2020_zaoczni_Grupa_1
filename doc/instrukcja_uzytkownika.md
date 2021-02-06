# Instrukcja Użytkownika

## Opis
- OpenNBP Analyzer to aplikacja mający na celu umożliwienie użytkownikom dokonywania analiz danych walutowych dostępnych w serwisie NBP.

## Wymagania
- Python, w wersji 3.0 lub wyższej.  

## Ogólne instrukcje
- Polecenia w aplikacji zatwierdzane są klawiszem Enter.

## Uruchomienie
- Należy wejść do folderu w którym znajdują się pliki aplikacji.
```
..\ZPI\ZPI2020_zaoczni_Grupa_1>
```  
- Następnie uruchomić plik run.py. Np. bezpośrdenio poprzez pythona.

## Funkcjonalności

### 1. Obliczanie sesji walutowych

#### Opis
-Wyświetlanie informacji o przebiegu kolejnych sesji (wzrostowe, spadkowe, bez zmian) dla wybranej waluty.

#### Dane wejściowe
* Kod Waluty (np. USD)
* Przedział Czasu (np. miesiąc)

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
- Wyświetlanie informacji o medianie, dominancie, odchyleniu standardowym oraz o współczynniku zmienności dla wybranej przez użytkownika waluty.

#### Dane wejściowe
* Kod Waluty (np. USD)
* Przedział Czasu (np. miesiąc)

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
- Wyświetlanie procentowego stosunku zmiany kursów dwóch wybranych przez użytkownika walut w wybranym przez niego okresie czasu.

#### Dane wejściowe
* Kod pierwszej waluty (np. GBP)
* Kod drugiej waluty (np. USD)
* Przedział Czasu (Miesiąc lub kwartał)

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
- Aby wyjść z programu należy wcisnąć klawisz 4.