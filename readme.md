# Open NBP Analyzer

## Skład zespołu
Scrum Master / Developer: Adrian Panas (@arszonto)  
Developer: Bartosz Soból (@ablesable)  
Tester: Jakub Kołaczyński (@kubak95)  
DevOps: Tobiasz Bielas (@TobiaszBielas)  

## Sprint Reviews
1. [20.01](https://github.com/IIS-ZPI/ZPI2020_zaoczni_Grupa_1/files/5791686/Sprint.20.01.Review.pdf)  
2. [21.01](https://github.com/IIS-ZPI/ZPI2020_zaoczni_Grupa_1/files/5792847/Sprint.21.01.Review.pdf)  
3. [21.02](https://github.com/IIS-ZPI/ZPI2020_zaoczni_Grupa_1/files/5862898/Sprint.21.02.Review.pdf)  
4. [21.03](https://github.com/IIS-ZPI/ZPI2020_zaoczni_Grupa_1/files/5862923/Sprint.21.03.Review.pdf)  
5. [21.04](https://github.com/IIS-ZPI/ZPI2020_zaoczni_Grupa_1/files/5899952/Sprint.21.04.Review.pdf)
6. [21.05](https://github.com/IIS-ZPI/ZPI2020_zaoczni_Grupa_1/files/5939766/Sprint.21.05.Review.pdf)
7. [21.06](https://github.com/IIS-ZPI/ZPI2020_zaoczni_Grupa_1/files/5977954/Sprint.21.06.Review.pdf)

## Informacje o procesie Scrum/Agile w projekcie  
* Każdy 'issue' czyli zadanie, w projekcie jest zamieszczone na tablicy (w modelu bazującym na Kanban).  
* Każde 'issue' ma odpowiedni numer identyfikacyjny, skróconą nazwę, opis wyjaśniający cel zadania, oraz listę kryteriów akceptacji, które należy wypełnić aby zadanie można było uznać za skończone i zdatne do review. Ponadto 'issue' są również oznaczone różnymi tagami, nazywanymi 'labels', które informują o zakresie prac (czego dotyczą - np. oznaczenie 'feature' oznaczna nową funkcjonalność aplikacji).  
* Wszystkie 'issue' są przypisane do kamieni milowych (milestones) w platofrmie github. Kamienie milowe odpowiadają kolejnym sprintom w procesie Agile. Sprinty/kamienie milowe są numerowane w następujący sposób: <Rok>.<Numer sprintu]>, np. "Sprint 21.01" oznacza pierwszy sprint w roku 2021.  
* Zespół pracuje w trybie sprintów trwających tydzień (z wyłączeniem przerwy świątecznej).  
* Zespół spotyka się na cotygodniowym spotkaniu, podzielonym na trzy części:  
  * Retro - podsumowanie zakończonego sprintu, dyskusja na temat tego co się udało a co nie, oraz z jakich powodów. Po zakończeniu dyskusji wyznaczane sa kroki celem rozwiązania problemów które ewentualnie wystąpiły i zostały podniesione podczas dyskusji. Na zakończenie zespół dokumentuje swoje prace w postaci, krótkiej, zwięzłej prezentacji przeznaczonej dla interesantów (np. product ownera).  
  * Spotkanie z PO i grupą - zespół, poprzez platformę MS Teams, wdzwania się na zajęcia z przedmiotu "Zarządzanie Projektami Informatycznymi" i przedstawia efekty swoich prac, wykorzystując przygotowaną wcześniej prezentację.  
  * Planning - w tej części zespół planuje działania na kolejny sprint. W skład tych planów wchodzi również 'wycenienie' zadań w systemie 'Story Points' (widoczne jako odpowiednni 'label' przy 'issue', np. '.P: 3' oznacza 3 punkty). Członkowie zespołu samodzielnie decydują które zadania zobowiązują się wykonać w kolejnym sprincie.  

#### Objaśnienie: 
Ze względu na formę pracy (między innymii ograniczoną możliwość kontaktu w tygodniu oraz fakt, że poszczególni członkowie pracują nad projektem w czasie wolnym), przyjęta została właśnie taka, niestandardowa forma organizacji spotkań. Natomiast cały zespół został 'przeszkolony' z tego jak faktycznie wygląda praca w metodyce Agile, które elementy zostały zmienione, jak w rzeczywistości wygląda np. "Retroperspective", czym są "Story Points" itd.  

## Konfiguracja CI  
System CI jest skonfigurowany w Github Actions. Z tego względu nie mamy żadnych dodatkowych danych konfiguracyjnych - wszystko jest dostępne dla każdego contributora repozytorium. 
* Korzystanie z automatycznego tagowania(gałęzie master i release):
  * wiadomość commit'a + #patch --> x.y.(z+1)
  * wiadomość commit'a + #minor --> x.(y+1).0
  * wiadomość commit'a + #major --> (x+1)).0.0

## Odnośniki
- [Issues](https://github.com/IIS-Mobile/PG2D_zima_2020_21_niestacjonarne_gr_1)  
- [Tablica Kanban](https://github.com/IIS-ZPI/ZPI2020_zaoczni_Grupa_1/projects/1)  
- [Specyfikacja techniczna](doc/specyfikacja_architektury.adoc)  
- [Instrukcja użytkownika](doc/instrukcja_uzytkownika.md)  

## Archiwum
Archiwalne branche z zadaniami poprzeadzającymi projekt znajdują się na następujących branchach:  
- legacy_master  
- legacy_develop  
- legacy_release  
Ponadto pod tagiem 1.2.0 znajduje się ostatnie wydanie z tego okresu.
