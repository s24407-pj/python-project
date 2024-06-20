import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualization:
    def __init__(self, data):
        self.data = data

    def create_histogram(self, column):
        try:
            self.data[column].plot(kind='hist')
            plt.title(f"Histogram of {column}")
            plt.xlabel(column)
            plt.ylabel("Frequency")
            plt.show()
        except KeyError as e:
            print(f"Niepoprawna kolumna: {e}")

    def create_scatter_plot(self, column1, column2):
        try:
            self.data.plot(kind='scatter', x=column1, y=column2)
            plt.title(f"Scatter Plot of {column1} vs {column2}")
            plt.xlabel(column1)
            plt.ylabel(column2)
            plt.show()
        except KeyError as e:
            print(f"Niepoprawna kolumna: {e}")

    def create_box_plot(self, column):
        try:
            sns.boxplot(data=self.data[column])
            plt.title(f"Box Plot of {column}")
            plt.xlabel(column)
            plt.show()
        except KeyError as e:
            print(f"Niepoprawna kolumna: {e}")

    def create_line_plot(self, column):
        try:
            self.data[column].plot(kind='line')
            plt.title(f"Line Plot of {column}")
            plt.xlabel('Index')
            plt.ylabel(column)
            plt.show()
        except KeyError as e:
            print(f"Niepoprawna kolumna: {e}")

    def create_bar_plot(self, column):
        try:
            self.data[column].value_counts().plot(kind='bar')
            plt.title(f"Bar Plot of {column}")
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.show()
        except KeyError as e:
            print(f"Niepoprawna kolumna: {e}")

    def create_heatmap(self, columns):
        try:
            corr = self.data[columns].corr()
            sns.heatmap(corr, annot=True, cmap='coolwarm')
            plt.title("Heatmap of Correlations")
            plt.show()
        except KeyError as e:
            print(f"Niepoprawne kolumny: {e}")
