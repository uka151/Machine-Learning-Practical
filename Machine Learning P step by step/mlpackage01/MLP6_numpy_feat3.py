import numpy as np
zr = np.zeros([3, 3])
print(zr)
print("print matrix 3*3 with 1 filled \n", zr +1)
ones = np.ones([3, 3])

print(ones)
# print matrix with 2 filled

print("matrix with 2 filled \n", ones+1)
print(ones.dtype)
print(type(ones))
# np.arange(1, 6)  create an array from given range
# in ML starting point inclusive & ending excluding

arr = np.arange(1, 8)
print(arr)

arr[1] = 4
print(arr)
# some predefine function provide statical operation
print("Sum of arr:", arr.sum())
print("Std of arr:", arr.std())
print("mean of arr :", arr.mean())
print("Largest element in arr :", arr.max())
print("Smallest element in arr :", arr.min())
print("Size of array :", arr.size)
print("Shape of arr :", arr.shape)
# print the index of nonzero element
print("all.nonzero():", arr.nonzero())
print(np.all(arr))
# Its check weather all the element is greater than zero or not
