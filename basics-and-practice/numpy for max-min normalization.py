import numpy as np

# 1D
# [10. 20. 30. 40. 50.]
x = np.arange(10, 51, 10, dtype=np.float64) # [10. 20. 30. 40. 50.]

x_max = np.max(x)
x_min = np.min(x)

x_norm = (x - x_min) / (x_max - x_min)
print(x_norm)


# 2D
matrix = np.array([
    [10, 100],
    [20, 200],
    [30, 300]
    ])

cols_min = np.min(matrix, axis=0) # [10, 100]
cols_max = np.max(matrix, axis=0) # [30, 300]
matrix_norm = (matrix - cols_min) / (cols_max - cols_min)
print(matrix_norm)