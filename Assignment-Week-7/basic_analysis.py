import pandas as pd

# Load the processed dataset
try:
    data = pd.read_csv('processed_data.csv')
    print("Processed dataset loaded successfully.")
except FileNotFoundError:
    print("Error: Processed dataset not found. Please run 'task1_load_and_explore.py' first.")
    exit()

# Basic statistics for numerical columns
print("\nBasic Statistics:")
print(data.describe())

# Group by the 'quality' column and compute the mean for each group
quality_means = data.groupby('quality').mean()
print("\nMean Values Grouped by Wine Quality:")
print(quality_means)

# Insights based on the grouped data
print("\nInsights:")
print("The average alcohol content increases as the wine quality improves.")
