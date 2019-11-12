import numpy as np
arr1 = np.array([1, 5, 3, 4])
arr2 = np.array([1, 2, 3, 4])
print("Sum of array:", arr1+arr2)
print("Sub of array:", arr1-arr2)
print("MUl of array:", arr1*arr2)
print("Div of array:", arr1 % arr2)
# shape must be same for calculation of both array
# arr3 = np.array([1, 2, 3])
# print(arr1+arr3)  # error due shape is not equal
arr4 = np.array([200, 400, 100, 306, 410])
# argsort() tell the index of element with sorted order

print(arr4.argsort())
arr4.sort()

print(arr4)
