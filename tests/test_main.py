import unittest
import os
import zipfile
import pandas as pd
import sys
import matplotlib
matplotlib.use('Agg')  # Use the Agg backend to prevent plotting windows from opening
import matplotlib.pyplot as plt

# Dodaj ścieżkę do katalogu src, aby Python mógł znaleźć moduły
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from data_loader import DataLoader
from data_analysis import DataAnalysis
from data_visualization import DataVisualization

class TestDataLoader(unittest.TestCase):
    def setUp(self):
        self.csv_content = """Name,Position,Age,Club,Height,Foot,Caps,Goals,MarketValue,Country
Alice,Manager,45,A,165,Right,100,30,5000000,Country1
Bob,Clerk,23,B,180,Left,50,5,300000,Country2
Charlie,CEO,50,C,170,Right,150,50,20000000,Country3
David,Clerk,34,A,175,Right,40,10,1000000,Country1"""
        
        self.csv_path = 'test_data.csv'
        with open(self.csv_path, 'w') as f:
            f.write(self.csv_content)
        
        self.zip_path = 'test_data.zip'
        with zipfile.ZipFile(self.zip_path, 'w') as zipf:
            zipf.write(self.csv_path)
        
    def tearDown(self):
        os.remove(self.csv_path)
        os.remove(self.zip_path)

    def test_data_loader(self):
        data_loader = DataLoader(self.csv_path)
        data = data_loader.load_data()
        self.assertIsNotNone(data)
        self.assertEqual(len(data), 4)
        self.assertIn('Name', data.columns)
        self.assertIn('Age', data.columns)

class TestDataAnalysis(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            'Name': ['Alice', 'Bob', 'Charlie', 'David'],
            'Position': ['Manager', 'Clerk', 'CEO', 'Clerk'],
            'Age': [45, 23, 50, 34],
            'Club': ['A', 'B', 'C', 'A'],
            'Height': [165, 180, 170, 175],
            'Foot': ['Right', 'Left', 'Right', 'Right'],
            'Caps': [100, 50, 150, 40],
            'Goals': [30, 5, 50, 10],
            'MarketValue': [5000000, 300000, 20000000, 1000000],
            'Country': ['Country1', 'Country2', 'Country3', 'Country1']
        })
        self.analysis = DataAnalysis(self.data)

    def test_explore_data(self):
        self.analysis.explore_data()

    def test_select_columns(self):
        selected_data = self.analysis.select_columns(['Name', 'Age'])
        self.assertEqual(selected_data.shape[1], 2)
        self.assertIn('Name', selected_data.columns)
        self.assertIn('Age', selected_data.columns)

    def test_filter_data(self):
        filtered_data = self.analysis.filter_data('Club', 'A')
        self.assertEqual(len(filtered_data), 2)
        self.assertTrue(all(filtered_data['Club'] == 'A'))

    def test_sort_data(self):
        sorted_data = self.analysis.sort_data('Age')
        self.assertEqual(sorted_data.iloc[0]['Name'], 'Bob')

    def test_aggregate_data(self):
        total_caps = self.analysis.aggregate_data('Caps', 'sum')
        self.assertEqual(total_caps, 340)

    def test_calculate_correlation(self):
        correlation = self.analysis.calculate_correlation('Caps', 'Goals')
        self.assertIsNotNone(correlation)

    def test_remove_duplicates(self):
        data_with_duplicates = pd.concat([self.data, self.data.iloc[[0]]])
        self.analysis.data = data_with_duplicates
        data_without_duplicates = self.analysis.remove_duplicates()
        self.assertEqual(len(data_without_duplicates), 4)

    def test_describe_column(self):
        description = self.analysis.describe_column('Age')
        self.assertIn('mean', description.index)

    def test_normalize_column(self):
        normalized_data = self.analysis.normalize_column('Age')
        self.assertAlmostEqual(normalized_data.min(), 0)
        self.assertAlmostEqual(normalized_data.max(), 1)

    def test_advanced_filter(self):
        filtered_data = self.analysis.advanced_filter('Age', '> 30')
        self.assertTrue(all(filtered_data['Age'] > 30))

class TestDataVisualization(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            'Name': ['Alice', 'Bob', 'Charlie', 'David'],
            'Position': ['Manager', 'Clerk', 'CEO', 'Clerk'],
            'Age': [45, 23, 50, 34],
            'Club': ['A', 'B', 'C', 'A'],
            'Height': [165, 180, 170, 175],
            'Foot': ['Right', 'Left', 'Right', 'Right'],
            'Caps': [100, 50, 150, 40],
            'Goals': [30, 5, 50, 10],
            'MarketValue': [5000000, 300000, 20000000, 1000000],
            'Country': ['Country1', 'Country2', 'Country3', 'Country1']
        })
        self.visualization = DataVisualization(self.data)

    def test_create_histogram(self):
        self.visualization.create_histogram('Age')
        plt.close()

    def test_create_scatter_plot(self):
        self.visualization.create_scatter_plot('Age', 'Height')
        plt.close()

    def test_create_box_plot(self):
        self.visualization.create_box_plot('Age')
        plt.close()

    def test_create_line_plot(self):
        self.visualization.create_line_plot('Age')
        plt.close()

    def test_create_bar_plot(self):
        self.visualization.create_bar_plot('Club')
        plt.close()

    def test_create_heatmap(self):
        self.visualization.create_heatmap(['Age', 'Height', 'Caps', 'Goals', 'MarketValue'])
        plt.close()

if __name__ == '__main__':
    unittest.main()
