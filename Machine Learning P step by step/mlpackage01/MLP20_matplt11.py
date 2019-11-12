# 3D scatter Plot
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import  axes3d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = np.random.randint(10, size=10)
z1 = np.random.randint(10, size=10)
x2 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, 10]
y2 = np.random.randint(-10, 0, size=10)
z2 = np.random.randint(10, size=10)
ax.scatter(x1, y1, z1, c='b', marker='o', label='blue')
ax.scatter(x2, y2, z2, c='r', marker='o', label='red')
ax.set_label("X axis")
ax.set_label("Y axis")
ax.set_label("Z axis")
plt.title("3D scatter plot")
plt.legend()
plt.show()