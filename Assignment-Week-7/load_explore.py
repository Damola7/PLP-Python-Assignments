import pandas as pd

# Load the dataset
try:
    data = pd.read_csv('winequality-red.csv', delimiter=';')  # Ensure the file name matches exactly
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: Dataset file not found.")
    exit()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit()

# Display the first few rows of the dataset
print("\nDataset Preview:")
print(data.head())

# Check the structure of the dataset
print("\nDataset Information:")
print(data.info())

# Check for missing values
missing_values = data.isnull().sum()
if missing_values.any():
    print("\nMissing Values Detected:")
    print(missing_values)
    data.fillna(data.mean(), inplace=True)
    print("Missing values have been filled with column means.")
else:
    print("\nNo missing values detected.")

# Save cleaned data for the next task
data.to_csv('processed_data.csv', index=False)
print("\nProcessed dataset saved as 'processed_data.csv'.")
