import numpy as np

a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
print(a)

# Get a specific element [row, col]
print(a[0, 6])
print(a[1, -2])

# Get specific row
print(a[0, :])

# Get specific column
print(a[:, 3])

# More complex [start: end: step]
print(a[0, 1: -1: 2])

# Change element
a[0, 3] = 20
print(a)

# Replace whole column
a[:, 2] = 22
print(a)

a[:, 2] = [0, 99]
print(a)
 