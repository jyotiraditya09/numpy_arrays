import numpy as np

"""one_array = np.ones((5, 3, 2), dtype=int)
print(one_array)

block = np.zeros((2, 3, 4))
block.reshape(6, 4)
print(block)


# Activity 1

matrix = np.arange(2, 11)
print(matrix)
new_matrix = matrix.reshape(3, 3)
print(new_matrix)
list_matrix = list(new_matrix)
print(type(list_matrix))

sqrt_matrix = np.array([])
matrix_2 = np.arange(1, 10)
for num in matrix_2:
    i = np.sqrt(num)
    sqrt_matrix[num] = i
print(sqrt_matrix)

"""
from scipy import stats
prices = np.array([13999,6298,10999,14999,7298,6385,8999,9999,9999,13868])
units = np.array([9,8,9,9,8,8,9,6,5,7])
prices_unit = prices * units
mean = np.mean(prices_unit)

modal = stats.mode(prices)

import random
radii = [random.randint(1, 10) for i in range(20)]

radii2 = np.array(radii)

area = np.pi * (radii2 ** 2)
