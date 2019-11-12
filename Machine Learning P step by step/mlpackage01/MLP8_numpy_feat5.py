import numpy as np
# Matrix operation
mat = np.array([[1, 2, 3, 4], [11, 12, 13, 14]])
print(mat)

# Transpose of Matrix
print(mat.transpose())
# identity matrix
print(np.eye(3))  # generate  identity matrix of 3*3

# find dot matrix
arr2 = np.ones([3, 3])
arr3 = np.dot(arr2, np.eye(3))
print(arr3)

