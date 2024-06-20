import pandas as pd

class DataAnalysis:
    def __init__(self, data):
        self.data = data

    def explore_data(self):
        print(self.data.info())
        print(self.data.describe())

    def select_columns(self, columns):
        try:
            selected_data = self.data[columns]
            return selected_data
        except KeyError as e:
            print(f"Niepoprawna kolumna: {e}")
            return None

    def filter_data(self, column, value):
        try:
            filtered_data = self.data[self.data[column] == value]
            return filtered_data
        except KeyError as e:
            print(f"Niepoprawna kolumna: {e}")
            return None

    def sort_data(self, column, ascending=True):
        try:
            sorted_data = self.data.sort_values(by=column, ascending=ascending)
            return sorted_data
        except KeyError as e:
            print(f"Niepoprawna kolumna: {e}")
            return None

    def aggregate_data(self, column, method):
        try:
            if method == 'sum':
                return self.data[column].sum()
            elif method == 'mean':
                return self.data[column].mean()
            elif method == 'median':
                return self.data[column].median()
            elif method == 'max':
                return self.data[column].max()
            elif method == 'min':
                return self.data[column].min()
            else:
                print("Niepoprawna metoda agregacji.")
                return None
        except KeyError as e:
            print(f"Niepoprawna kolumna: {e}")
            return None

    def calculate_correlation(self, column1, column2):
        try:
            correlation = self.data[[column1, column2]].corr().iloc[0, 1]
            return correlation
        except KeyError as e:
            print(f"Niepoprawne kolumny: {e}")
            return None

    def remove_duplicates(self):
        self.data = self.data.drop_duplicates()
        return self.data

    def describe_column(self, column):
        try:
            description = self.data[column].describe()
            return description
        except KeyError as e:
            print(f"Niepoprawna kolumna: {e}")
            return None

    def normalize_column(self, column):
        try:
            self.data[column] = (self.data[column] - self.data[column].min()) / (self.data[column].max() - self.data[column].min())
            return self.data[column]
        except KeyError as e:
            print(f"Niepoprawna kolumna: {e}")
            return None

    def advanced_filter(self, column, condition):
        try:
            filtered_data = self.data.query(f"{column} {condition}")
            return filtered_data
        except KeyError as e:
            print(f"Niepoprawna kolumna: {e}")
            return None
