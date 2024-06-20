# Analiza Danych

## Opis projektu

Ten projekt służy do wczytywania, analizy i wizualizacji danych z plików CSV zawartych w archiwach ZIP. Projekt składa się z kilku modułów odpowiedzialnych za różne etapy przetwarzania danych:

- `DataLoader`: Moduł odpowiedzialny za wczytywanie danych z plików CSV.
- `DataAnalysis`: Moduł odpowiedzialny za podstawowe operacje analizy danych, takie jak sortowanie, filtrowanie, agregacja, korelacja, usuwanie duplikatów, statystyki opisowe, normalizacja i zaawansowane filtrowanie.
- `DataVisualization`: Moduł odpowiedzialny za wizualizację danych, w tym histogramy, wykresy rozrzutu, wykresy pudełkowe, wykresy liniowe, wykresy słupkowe i mapy cieplne.

## Wymagania

- Python 3.7 lub nowszy

### Instalacja zależności

W projekcie znajduje się plik `requirements.txt`, który zawiera wszystkie wymagane pakiety. Możesz zainstalować te pakiety za pomocą poniższego polecenia:

```bash
pip install -r requirements.txt
```

Zawartość pliku `requirements.txt`:

```
pandas
numpy
matplotlib
seaborn
```

## Uruchamianie programu

Aby uruchomić główny program, użyj poniższego polecenia:

```bash
python src/main.py
```

## Testowanie

Aby uruchomić testy jednostkowe, użyj poniższego polecenia:

```bash
python -m unittest tests/test_main.py
```

## Instrukcja obsługi

1. **Wybór pliku ZIP**:

   - Po uruchomieniu programu, zostaniesz poproszony o wybranie pliku ZIP zawierającego dane do analizy.

2. **Eksploracja danych**:

   - Po wczytaniu danych, program wyświetli podstawowe informacje o danych, takie jak typy kolumn, liczba niepustych wartości oraz statystyki opisowe.

3. **Wybór metody analizy**:

   - Program wyświetli dostępne metody analizy danych. Możesz wybrać jedną z poniższych opcji:
     1. Sortowanie
     2. Filtrowanie
     3. Agregacja
     4. Korelacja
     5. Usuwanie duplikatów
     6. Statystyki opisowe
     7. Normalizacja
     8. Zaawansowane filtrowanie
     9. Wizualizacja danych
     10. Zakończ

4. **Sortowanie**:

   - Wybierz kolumnę do sortowania i kierunek sortowania (rosnąco lub malejąco).

5. **Filtrowanie**:

   - Wybierz kolumnę i wartość, według której chcesz filtrować dane.

6. **Agregacja**:

   - Wybierz kolumnę i metodę agregacji (suma, średnia, mediana, maksimum, minimum).

7. **Korelacja**:

   - Wybierz dwie kolumny, dla których chcesz obliczyć współczynnik korelacji.

8. **Usuwanie duplikatów**:

   - Program usunie duplikaty z danych.

9. **Statystyki opisowe**:

   - Wybierz kolumnę, dla której chcesz wyświetlić statystyki opisowe.

10. **Normalizacja**:

    - Wybierz kolumnę, którą chcesz znormalizować.

11. **Zaawansowane filtrowanie**:

    - Wybierz kolumnę i warunek filtrowania (np. `> 10`).

12. **Wizualizacja danych**:
    - Wybierz jedną z dostępnych wizualizacji:
      1. Histogram
      2. Scatter Plot (Wykres rozrzutu)
      3. Box Plot (Wykres pudełkowy)
      4. Line Plot (Wykres liniowy)
      5. Bar Plot (Wykres słupkowy)
      6. Heatmap (Mapa cieplna)

## Wyjaśnienie zastosowanych metod

### a. Dlaczego zastosowane w programie metody są dostosowane do wybranego typu danych i prezentowanego zagadnienia analitycznego?

Metody zastosowane w programie zostały dobrane tak, aby umożliwić kompleksową analizę danych liczbowych oraz kategorycznych. Zostały one wybrane ze względu na ich powszechne zastosowanie w analizie danych i łatwość interpretacji wyników. Przykładowe metody i ich zastosowanie:

- **Sortowanie**: Umożliwia uporządkowanie danych według wartości wybranej kolumny, co jest przydatne przy analizie porównawczej.
- **Filtrowanie**: Umożliwia wyselekcjonowanie podzbioru danych spełniających określone kryteria, co jest użyteczne przy analizie skupionej na określonych warunkach.
- **Agregacja**: Umożliwia obliczenie wartości sumarycznych, średnich i innych statystyk dla wybranych kolumn, co jest przydatne przy podsumowywaniu danych.
- **Korelacja**: Umożliwia zbadanie zależności między dwiema zmiennymi, co jest ważne przy analizie współzależności.
- **Usuwanie duplikatów**: Zapewnia, że analiza jest przeprowadzana na unikalnych rekordach, co zwiększa wiarygodność wyników.
- **Statystyki opisowe**: Dostarczają podstawowych informacji o rozkładzie danych, takich jak średnia, mediana, odchylenie standardowe.
- **Normalizacja**: Przekształca dane do wspólnej skali, co jest przydatne przy porównywaniu różnych zestawów danych.
- **Zaawansowane filtrowanie**: Pozwala na bardziej skomplikowane zapytania filtrujące, co umożliwia dokładniejszą analizę.
- **Wizualizacja danych**: Wykresy takie jak histogramy, wykresy rozrzutu, pudełkowe, liniowe, słupkowe i mapy cieplne umożliwiają łatwe zrozumienie danych i wyciągnięcie wniosków.

### b. Wyjaśnienie zastosowanych rozwiązań programistycznych

Projekt został zorganizowany w sposób modułowy, z wyraźnym podziałem na różne etapy przetwarzania danych:

- **Struktura i relacje klas**:

  - `DataLoader`: Klasa odpowiedzialna za wczytywanie danych z plików CSV. Oddziela proces wczytywania danych od ich analizy i wizualizacji, co zwiększa modularność kodu.
  - `DataAnalysis`: Klasa zawierająca metody analizy danych. Metody te operują na DataFrame'ach Pandas, co umożliwia wydajną manipulację i analizę danych.
  - `DataVisualization`: Klasa zawierająca metody do wizualizacji danych przy użyciu biblioteki Matplotlib i Seaborn. Dzięki temu wizualizacje są klarowne i profesjonalnie wyglądające.

- **Wzorce projektowe**:
  - **Modularność**: Projekt został podzielony na moduły (wczytywanie danych, analiza, wizualizacja), co ułatwia rozwój, testowanie i konserwację kodu.
  - **Separacja logiki**: Logika wczytywania, analizy i wizualizacji danych jest oddzielona, co pozwala na łatwe modyfikowanie i rozbudowę każdej części projektu bez wpływu na pozostałe moduły.
  - **Testowanie**: Przygotowano testy jednostkowe dla każdej klasy i jej metod, co zapewnia, że poszczególne części projektu działają poprawnie i zgodnie z oczekiwaniami.

## Przykładowe dane

W katalogu `data` powinien znajdować się plik ZIP zawierający dane w formacie CSV. Przykładowy plik ZIP może wyglądać następująco:

```
data/
|-- test_data.zip
```

Plik `test_data.csv` wewnątrz

archiwum ZIP może zawierać następujące dane:

```
Name,Position,Age,Club,Height,Foot,Caps,Goals,MarketValue,Country
Alice,Manager,45,A,165,Right,100,30,5000000,Country1
Bob,Clerk,23,B,180,Left,50,5,300000,Country2
Charlie,CEO,50,C,170,Right,150,50,20000000,Country3
David,Clerk,34,A,175,Right,40,10,1000000,Country1
```
