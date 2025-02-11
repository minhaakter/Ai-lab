import numpy as np
matrix = np.random.randint(1, 100, (5, 5))
row_sums = np.sum(matrix, axis=1)
print("Matrix:\n", matrix)
print("Row-wise Sums:", row_sums)