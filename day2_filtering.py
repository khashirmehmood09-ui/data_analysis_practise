import pandas as pd

# Load dataset directly from online
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# First 5 rows
print("\n--- First 5 rows ---")
print(df.head())

# Shape of dataset
print("\n--- Shape of dataset ---")
print(df.shape)

# Column names
print("\n--- Column names ---")
print(df.columns)

# Summary statistics
print("\n--- Summary statistics ---")
print(df.describe())

# Unique species
print("\n--- Unique species ---")
print(df['species'].unique())

print("\n--- Count of each species ---")
print(df['species'].value_counts())

# Filtering examples
print("\n--- Only Setosa ---")
print(df[df['species'] == 'setosa'].head())

print("\n--- Sepal Length > 5 ---")
print(df[df['sepal_length'] > 5.0].head())

# Combined conditions
print("\n--- Setosa with Sepal Length > 5 ---")
print(df[(df['species'] == 'setosa') & (df['sepal_length'] > 5.0)].head())
