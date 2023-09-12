import numpy as np

# exercise: Create following matrix
"""
    1 1 1 1 1
    1 0 0 0 1
    1 0 9 0 1
    1 0 0 0 1
    1 1 1 1 1
"""

a = np.ones((5, 5))
a[1, 1:4] = 0
a[2, 1:4:2] = 0
a[3, 1:4] = 0
a[2, 2] = 9

print(a)

b = np.ones((5, 5))
z = np.zeros((3, 3))
z[1, 1] = 9
b[1:4, 1:4] = z

print(b)
