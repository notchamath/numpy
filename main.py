import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1.0, 2.0, 3.0], [0.4, 0.5, 0.6]])

print(a)
print(b)

# Get dimensions
print(a.ndim)
print(b.ndim)

# Get Shape
print(a.shape)
print(b.shape)

# Data type
print(a.dtype)
print(b.dtype)

# Declare type
c = np.array([1, 2, 3], dtype="int16")

print(c.dtype)

# Size of each element in bytes
print(a.itemsize)
print(b.itemsize)
print(c.itemsize)

# Total number of elements
print(b.size)

# Total size of the array
print(b.nbytes)

