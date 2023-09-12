import numpy as np

# Read from a text file
a = np.genfromtxt("data.txt", delimiter=",")
print(a)

# Change data type
b = a.astype("int32")
print(b)

# Boolean masking and advanced indexing
print(b > 50)

c = b[b > 50]
print(c)

d = np.array([1,2,3,4,5,6,7,8])
e = d[[1,2,5]]
print(e)

print(np.any(b > 50, axis=0))
print(np.any(b > 50, axis=1))

print((b > 50) & (b < 100))
print(~(b > 50) & (b < 100))
