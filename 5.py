import numpy as np

# Reorganizing Arrays
before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

# Reshaped array has to have the same num of elements as original
after = before.reshape((4, 2))
print(after)

# Vertically stacking vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
print(np.vstack([v1, v2]))

# Horizontally stacking vectors
v1 = np.zeros((2,4))
v2 = np.ones((2,2))
print(np.hstack([v1, v2]))
