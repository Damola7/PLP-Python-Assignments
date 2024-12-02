import pandas as pd
import matplotlib.pyplot as plt

# Load the processed dataset
try:
    data = pd.read_csv('processed_data.csv')
    print("Processed dataset loaded successfully.")
except FileNotFoundError:
    print("Error: Processed dataset not found. Please run 'task1_load_and_explore.py' first.")
    exit()

# Group by 'quality' and get the mean alcohol content
quality_means = data.groupby('quality')['alcohol'].mean()

# Line Chart
plt.plot(quality_means.index, quality_means, marker='o', color='blue')
plt.title('Average Alcohol Content by Wine Quality')
plt.xlabel('Wine Quality')
plt.ylabel('Alcohol (%)')
plt.show()

# Bar Chart
plt.bar(quality_means.index, quality_means)
plt.title('Average Alcohol by Wine Quality')
plt.xlabel('Wine Quality')
plt.ylabel('Alcohol (%)')
plt.show()

# Histogram
plt.hist(data['pH'], bins=20, color='purple')
plt.title('Distribution of pH Values')
plt.xlabel('pH')
plt.ylabel('Frequency')
plt.show()

# Scatter Plot
plt.scatter(data['alcohol'], data['density'], alpha=0.5)
plt.title('Alcohol vs. Density')
plt.xlabel('Alcohol (%)')
plt.ylabel('Density')
plt.show()
