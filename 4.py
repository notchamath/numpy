import numpy as np

# How to copy a np array, a=b will only create a pointer
a = np.array([1, 2, 3])
b = a.copy()
b[0] = 100

print(a)
print(b)

# Math operations can be applied to all elements at once
a = np.array([1, 2, 3, 4])
print(a)
print(a + 2)
print(a * 2)
print(a - 2)
print(a ** 2)

a += 2
print(a)

b = [10, 10, 10, 10]
print(a + b)

print(np.cos(a))

# Linear Algebra
c = np.ones((2, 3))
print(c)
d = np.full((3, 2), 2)
print(d)

print(np.matmul(c, d))

# Statistics
stats = np.array([[1,2,3],[4,5,6]])
print(np.min(stats))
print(np.max(stats))
print(np.min(stats, axis=1))
print(np.sum(stats))
