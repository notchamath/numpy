import numpy as np

a = np.full((6, 5), 5)
print(a[2:4, :2])
print(a[[0,1,2,3],[1,2,3,4]])
