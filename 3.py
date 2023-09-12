import numpy as np

# Initializing Different types of arrays

# All 0's matrix
a = np.zeros((5))
print(a)
b = np.zeros((4, 3))
print(b)

# All 1's matrix
a = np.ones((5))
print(a)
b = np.ones((4, 3))
print(b)

# All any-other-num's matrix
a = np.full((5), 88)
print(a)
b = np.full((4, 3), 88)
print(b)

# Create array of nums modeling the shape of another array
c = np.full_like(b, 4)
print(c)

# Create array of random decimals between 0 and 1
d = np.random.rand(2, 4)
print(d)

# Create array of random int between 0 and 1. randint(low, high, size=(?,?))
f = np.random.randint(2, 5, size=(3, 6))
print(f)

# Identity Matrix
g = np.identity(5)
print(g)

# Repeat an array
arr = np.array([[1,2,3], [4,5,6]])
r1 = np.repeat(arr, 3, 1)
print(r1)
