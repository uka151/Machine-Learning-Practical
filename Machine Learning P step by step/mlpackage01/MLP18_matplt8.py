import matplotlib.pyplot as plt
# Look index 4 and 6, which demonstrate
# overlapping cases.
x1 = [1, 3, 4, 5, 6, 7, 9]
y1 = [4, 7, 2, 4, 7, 8, 3]
x2 = [2, 4, 6, 8, 10]
y2 = [5, 6, 2, 6, 2]
plt.bar(x2, y2, label='Green Bar', color='g')
plt.bar(x1, y1, label='Red Bar', color='r')

plt.title("Bar Diagram")
plt.xlabel("Bar number")
plt.ylabel("Height of Bar")
plt.legend()
plt.show()