import numpy as np
import matplotlib.pyplot as plt
filename = 'indians-diabetes.data.csv'
data = np.loadtxt(filename, delimiter=',')
x1 = np.array(data[:, 0])
y1 = np.array(data[:, -1])
x2 = np.array(data[:, 2])
y2 = np.array(data[:, -1])
plt.plot(x1, y1, marker='.', markersize=18, linestyle='none', color='blue')
plt.plot(x2, y2, marker='.', markersize=19, linestyle='none', color='red')

plt.title("indians diabetes")
plt.show()