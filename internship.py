import pandas as pd

# Replace 'path_to_your_file.csv' with the actual path to your CSV file
file_path = 'C:\Users\divya\Desktop\cognifyz'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("C:\Users\divya\Desktop\cognifyz".csv)

# Display the number of rows and columns
num_rows, num_columns = df.shape
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")