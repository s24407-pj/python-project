import os
import pandas as pd
from data_loader import DataLoader
from data_analysis import DataAnalysis
from data_visualization import DataVisualization



def main():
    try:
        data_directory = 'data'
        available_files = data_loader.list_zip_files_in_directory(data_directory)
        
        if not available_files:
            print("Brak dostępnych plików ZIP w katalogu 'data'.")
            return
        
        print("Dostępne pliki ZIP:")
        for idx, file in enumerate(available_files):
            print(f"{idx + 1}. {file}")
        
        file_choice = int(input("Wybierz numer pliku ZIP do wczytania: ")) - 1
        
        if file_choice < 0 or file_choice >= len(available_files):
            print("Niepoprawny wybór pliku.")
            return
        
        zip_path = os.path.join(data_directory, available_files[file_choice])
        
        csv_path = data_loader.extract_csv_from_zip(zip_path)
        
        if csv_path is None:
            print("Błąd podczas rozpakowywania i wczytywania pliku CSV.")
            return
        
        print(f"Wczytywanie danych z pliku: {csv_path}")
        data_loader = DataLoader(csv_path)
        data = data_loader.load_data()
        
        if data is None:
            print("Błąd podczas wczytywania danych.")
            return
        
        print("Eksploracja danych...")
        data_analysis = DataAnalysis(data)
        data_analysis.explore_data()

        columns = sorted(list(data.columns))
        data_visualization = DataVisualization(data)
        
        while True:
            print("\nDostępne metody analizy danych:")
            print("1. Sortowanie")
            print("2. Filtrowanie")
            print("3. Agregacja")
            print("4. Korelacja")
            print("5. Usuwanie duplikatów")
            print("6. Statystyki opisowe")
            print("7. Normalizacja")
            print("8. Zaawansowane filtrowanie")
            print("9. Wizualizacja danych")
            print("0. Zakończ")

            try:
                analysis_choice = int(input("Wybierz metodę analizy (0-9): "))
            except ValueError:
                print("Niepoprawny wybór. Proszę wybrać numer od 0 do 9.")
                continue

            if analysis_choice == 0:
                break

            
            print("Dostępne kolumny:")
            for idx, column in enumerate(columns):
                print(f"{idx + 1}. {column}")

            try:
                if analysis_choice in [1, 2, 3, 4, 6, 7, 8]:
                    column_choice = int(input("Wybierz numer kolumny do analizy: ")) - 1
                    if column_choice < 0 or column_choice >= len(columns):
                        print("Niepoprawny wybór kolumny.")
                        continue
                    column = columns[column_choice]

                if analysis_choice == 1:
                    sort_order = input("Wybierz kierunek sortowania (asc/desc): ").strip().lower()
                    ascending = sort_order == 'asc'
                    sorted_data = data_analysis.sort_data(column, ascending)
                    print(f"Dane zostały posortowane według kolumny '{column}' w porządku {'rosnącym' if ascending else 'malejącym'}.")
                    print(sorted_data)
                elif analysis_choice == 2:
                    value = input(f"Podaj wartość do filtrowania w kolumnie '{column}': ").strip()
                    filtered_data = data_analysis.filter_data(column, value)
                    print(f"Dane po filtrowaniu w kolumnie '{column}' z wartością '{value}':")
                    print(filtered_data)
                elif analysis_choice == 3:
                    print("Dostępne metody agregacji: sum, mean, median, max, min")
                    method = input("Podaj metodę agregacji: ").strip()
                    result = data_analysis.aggregate_data(column, method)
                    print(f"Wynik agregacji w kolumnie '{column}' metodą '{method}': {result}")
                elif analysis_choice == 4:
                    column_choice_2 = int(input("Wybierz numer drugiej kolumny do korelacji: ")) - 1
                    if column_choice_2 < 0 or column_choice_2 >= len(columns):
                        print("Niepoprawny wybór kolumny.")
                        continue
                    column2 = columns[column_choice_2]
                    if not (pd.api.types.is_numeric_dtype(data[column]) and pd.api.types.is_numeric_dtype(data[column2])):
                        print("Obie kolumny muszą być typu numerycznego.")
                        continue
                    correlation = data_analysis.calculate_correlation(column, column2)
                    print(f"Korelacja między kolumną '{column}' a '{column2}': {correlation}")
                elif analysis_choice == 5:
                    data_without_duplicates = data_analysis.remove_duplicates()
                    print("Dane po usunięciu duplikatów:")
                    print(data_without_duplicates)
                elif analysis_choice == 6:
                    description = data_analysis.describe_column(column)
                    print(f"Statystyki opisowe dla kolumny '{column}':")
                    print(description)
                elif analysis_choice == 7:
                    normalized_data = data_analysis.normalize_column(column)
                    print(f"Znormalizowane dane w kolumnie '{column}':")
                    print(normalized_data)
                elif analysis_choice == 8:
                    condition = input(f"Podaj warunek filtrowania dla kolumny '{column}' (np. > 10): ").strip()
                    filtered_data = data_analysis.advanced_filter(column, condition)
                    print(f"Dane po filtrowaniu w kolumnie '{column}' z warunkiem '{condition}':")
                    print(filtered_data)
                elif analysis_choice == 9:
                    print("Dostępne analizy: 1) Histogram, 2) Scatter Plot, 3) Box Plot, 4) Line Plot, 5) Bar Plot, 6) Heatmap")
                    vis_choice = int(input("Wybierz rodzaj analizy (1-6): "))
                    if vis_choice == 1:
                        column_choice = int(input("Wybierz numer kolumny do histogramu: ")) - 1
                        if column_choice < 0 or column_choice >= len(columns):
                            print("Niepoprawna kolumna.")
                            continue
                        column = columns[column_choice]
                        data_visualization.create_histogram(column)
                    elif vis_choice == 2:
                        column_choice_1 = int(input("Wybierz numer pierwszej kolumny do Scatter Plot: ")) - 1
                        if column_choice_1 < 0 or column_choice_1 >= len(columns):
                            print("Niepoprawna kolumna.")
                            continue
                        column1 = columns[column_choice_1]
                        column_choice_2 = int(input("Wybierz numer drugiej kolumny do Scatter Plot: ")) - 1
                        if column_choice_2 < 0 or column_choice_2 >= len(columns):
                            print("Niepoprawna kolumna.")
                            continue
                        column2 = columns[column_choice_2]
                        if not (pd.api.types.is_numeric_dtype(data[column1]) and pd.api.types.is_numeric_dtype(data[column2])):
                            print("Obie kolumny muszą być typu numerycznego.")
                            continue
                        data_visualization.create_scatter_plot(column1, column2)
                    elif vis_choice == 3:
                        column_choice = int(input("Wybierz numer kolumny do Box Plot: ")) - 1
                        if column_choice < 0 or column_choice >= len(columns):
                            print("Niepoprawna kolumna.")
                            continue
                        column = columns[column_choice]
                        data_visualization.create_box_plot(column)
                    elif vis_choice == 4:
                        column_choice = int(input("Wybierz numer kolumny do Line Plot: ")) - 1
                        if column_choice < 0 or column_choice >= len(columns):
                            print("Niepoprawna kolumna.")
                            continue
                        column = columns[column_choice]
                        data_visualization.create_line_plot(column)
                    elif vis_choice == 5:
                        column_choice = int(input("Wybierz numer kolumny do Bar Plot: ")) - 1
                        if column_choice < 0 or column_choice >= len(columns):
                            print("Niepoprawna kolumna.")
                            continue
                        column = columns[column_choice]
                        data_visualization.create_bar_plot(column)
                    elif vis_choice == 6:
                        heatmap_columns = input("Wprowadź numery kolumn do Heatmap (oddzielone przecinkami): ").split(',')
                        heatmap_columns = [columns[int(choice.strip()) - 1] for choice in heatmap_columns if choice.strip().isdigit() and 0 < int(choice.strip()) <= len(columns)]
                        # Walidacja, aby upewnić się, że kolumny są numeryczne
                        heatmap_columns = [col for col in heatmap_columns if pd.api.types.is_numeric_dtype(data[col])]
                        if len(heatmap_columns) > 1:
                            data_visualization.create_heatmap(heatmap_columns)
                        else:
                            print("Musisz wybrać więcej niż jedną kolumnę i wszystkie kolumny muszą być numeryczne.")
                    else:
                        print("Niepoprawny wybór analizy.")
                else:
                    print("Niepoprawny wybór metody analizy.")
            except Exception as e:
                print(f"Wystąpił błąd: {e}")

    except Exception as e:
        print(f"Wystąpił błąd w głównym procesie: {e}")

if __name__ == "__main__":
    main()
