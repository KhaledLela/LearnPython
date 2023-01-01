"""
https://stackoverflow.com/questions/74951164/printing-specific-rows-of-an-array-in-python
"""
import numpy as np

A = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25]])

J = [[1, 4]]
B = A[J[0]]
print([B])
