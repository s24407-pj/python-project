# Analiza Danych

## Opis projektu

Ten projekt służy do wczytywania, analizy i wizualizacji danych z plików CSV zawartych w archiwach ZIP. Projekt składa się z kilku modułów odpowiedzialnych za różne etapy przetwarzania danych:

- `DataLoader`: Moduł odpowiedzialny za wczytywanie danych z plików CSV.
- `DataAnalysis`: Moduł odpowiedzialny za podstawowe operacje analizy danych, takie jak sortowanie, filtrowanie, agregacja, korelacja, usuwanie duplikatów, statystyki opisowe, normalizacja i zaawansowane filtrowanie.
- `DataVisualization`: Moduł odpowiedzialny za wizualizację danych, w tym histogramy, wykresy rozrzutu, wykresy pudełkowe, wykresy liniowe, wykresy słupkowe i mapy cieplne.

## Wymagania

- Python 3.7 lub nowszy
- Pandas
- Matplotlib
- Unittest

Możesz zainstalować wymagane pakiety, uruchamiając:

```bash
pip install pandas matplotlib
```

## Struktura katalogów

Struktura katalogów projektu powinna wyglądać następująco:

```
python-project/
|-- src/
|   |-- data_loader.py
|   |-- data_analysis.py
|   |-- data_visualization.py
|   |-- main.py
|-- tests/
|   |-- test_main.py
|-- data/
|   |-- test_data.zip (lub inne pliki ZIP zawierające dane CSV)
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

## Przykładowe dane

W katalogu `data` powinien znajdować się plik ZIP zawierający dane w formacie CSV. Przykładowy plik ZIP może wyglądać następująco:

```
data/
|-- test_data.zip
```

Plik `test_data.csv` wewnątrz archiwum ZIP może zawierać następujące dane:

```
Name,Position,Age,Club,Height,Foot,Caps,Goals,MarketValue,Country
Alice,Manager,45,A,165,Right,100,30,5000000,Country1
Bob,Clerk,23,B,180,Left,50,5,300000,Country2
Charlie,CEO,50,C,170,Right,150,50,20000000,Country3
David,Clerk,34,A,175,Right,40,10,1000000,Country1
```
