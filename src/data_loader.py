import os
import zipfile
import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        try:
            data = pd.read_csv(self.file_path)
            return data
        except Exception as e:
            print(f"Błąd podczas wczytywania danych: {e}")
            return None
        
    def list_zip_files_in_directory(directory):
        try:
            files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.endswith('.zip')]
            return files
        except Exception as e:
            print(f"Nie udało się uzyskać listy plików: {e}")
            return []

    def extract_csv_from_zip(zip_path, extract_to='extracted'):
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
                csv_file_name = os.path.splitext(os.path.basename(zip_path))[0] + '.csv'
                csv_path = os.path.join(extract_to, csv_file_name)
                if os.path.isfile(csv_path):
                    return csv_path
                else:
                    print(f"Plik {csv_file_name} nie został znaleziony w archiwum.")
                    return None
        except Exception as e:
            print(f"Nie udało się rozpakować pliku: {e}")
            return None