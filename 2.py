import numpy as np

# 3D array
a = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(a)

# Get specific element (Work outside in)
print(a[0, 1, 1])

# Replace
a[:, 1, :] = [[9,9], [8,8]]
print(a)
