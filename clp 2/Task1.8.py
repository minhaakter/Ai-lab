import pandas as pd
import numpy as np

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

data = []
for i in range(rows):
    row = []
    for j in range(cols):
        value = input(f"Enter value for row {i+1}, column {j+1} (or leave empty for NaN): ")
        row.append(float(value) if value else np.nan)
    data.append(row)

df = pd.DataFrame(data)
df.fillna(df.mean(), inplace=True)

print("Dataset after Filling Missing Values:\n", df)