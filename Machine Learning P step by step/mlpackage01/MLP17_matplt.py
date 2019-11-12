# stack plot

import matplotlib.pyplot as plt
index = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr1 = [23, 40, 28, 43, 8, 44, 43, 18, 17]
arr2 = [17, 30, 22, 14, 17, 17, 29, 22, 30]
arr3 = [15, 31, 18, 22, 18, 19, 13, 32, 39]
plt.plot([], [], label='d1', color='r')
plt.plot([], [], label='d2', color='g')
plt.plot([], [], label='d3', color='b')
plt.stackplot(index, arr1, arr2, arr3, colors=['r', 'g', 'b'])
plt.title("Stack Plot")
plt.legend()
plt.show()