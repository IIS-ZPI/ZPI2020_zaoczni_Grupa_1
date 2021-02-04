## Instrukcja Użytkownika
- Polecenia w aplikacji zatwierdzane są klawiszem Enter.

### Opis
OpenNBP Analyzer to aplikacja mający na celu umożliwienie użytkownikom dokonywania analiz danych walutowych dostępnych w serwisie NBP.

### Wymagania
- Zainstalowany python w wersji 3.0 lub wyższy. 

### Instalacja

- Należy pobrać wersję release dostępną w repozytorium (Obecna wersja 1.3.1). Oraz wypakować jej zawartość do docelowego folderu.

### Uruchomienie
- Za pomocą komendy poleceń należy znaleźć się w folderze docelowym.
```
..\ZPI\ZPI2020_zaoczni_Grupa_1>
```  
Uruchomić aplikację poprzez komendę:
```
..\ZPI\ZPI2020_zaoczni_Grupa_1> python run.py
```
## Funkcjonalności

### 1. Obliczanie sesji walutowych

#### Opis
Funkcjonalność ta pozwala uzyskać informacje o przebiegu kolejnych sesji (wzrostowa, spadkowa, bez zmian) dla wybranej waluty.

#### Dane wejściowe
* Kod Waluty (np. USD)
* Przedział Czasu (np. miesiąc)

#### Rezultaty

```
Wynik: 
Dni wzrostu: 11
Dni spadkowe: 10
Dni bez zmian: 0
```
#### Przykład użycia
1. Użytkownik wprowadza kod waluty "USD"
```
Podaj walutę (kod, np. USD): USD
```
2. Użytkownik wybiera numer odpowiadający przedziałowi czasowemu dwóch tygodni.

```
Podaj okres czasu: 2
```
3. Otrzymuje wynik w postaci sumy dni wzrostowych, spadkowych i bez zmiany.

```
Wynik: 
Dni wzrostu: 4
Dni spadkowe: 5
Dni bez zmian: 0
```
4. Aby kontynuować działanie programu wciska przycisk Enter.

### 2. Obliczanie miar statystycznych

#### Opis
Funkcjonalność ta pozwala uzyskać informacje o medianie, dominancie, odchyleniu standardowym oraz o współczynniku zmienności dla wybranej waluty.

#### Dane wejściowe
* Kod Waluty (np. USD)
* Przedział Czasu (np. miesiąc)

#### Rezultaty
```
Mediana wyników: 3.74
Dominanta wyników:3.73
Odchylenie standardowe zbioru : 0.011
Współczynnik zmienności zbioru : 0.294
```
#### Przykład użycia
1. Użytkownik wprowadza kod waluty GBP i numer odpowiadający przedziałowi czasowemu dla którego interesują go statystyka (3 - miesiąc).

2. Wynik prezentuje się następująco:
```
Mediana wyników: 5.12
Dominanta wyników:5.12
Odchylenie standardowe zbioru : 0.018
Współczynnik zmienności zbioru : 0.352
```
3. Wcisnąć przycisk Enter by kontynować działanie aplikacji.

### 3. Rozkład zmian pomiędzy dwoma walutami

#### Opis
Funkcjonalność ta pozwala na porównanie stosunku zmiany kursów dwóch wybranych przez użytkownika walut w wybranym okresie czasu.

#### Dane wejściowe
* Kod pierwszej waluty (np. GBP)

* Kod drugiej waluty (np. USD)

* Przedział Czasu (Miesiąc lub kwartał)

#### Rezultaty
```
Zmiana kursu GBP względem USD: -0.2664%
```

#### Przykłady Użycia

1. Użytkownik wprowadza kod pierwszej waluty - GBP

2. Później kod drugiej waluty - USD
```
Podaj drugą walutę (kod, np. USD):USD
```
3. Wpisuje liczbę odpowiadającą kwartałowi czyli 2.

4. Otrzymuje wynik procentowy stosunku zmian jednej waluty do drugiej
```
Zmiana kursu GBP względem USD: 5.1279%
```
5. Zatwierdza przyciskiem Enter chęć dalszego korzystania z programu.

### Wyjście z programu.

Aby wyjść z programu należy wcisnąć kombinację klawiszy Ctrl + C.