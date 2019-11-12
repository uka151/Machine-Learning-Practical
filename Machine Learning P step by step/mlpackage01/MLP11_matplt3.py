import matplotlib.pyplot as plt
#plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'go-', label='Squared', Linewidth=4)
#plt.plot([1, 2, 3, 4, 5], [1, 8, 27, 64, 81], 'ro-', Label='Cube', linewidth=4)
x1 = [1, 2, 3]
y1 = [1, 4, 9]
x2 = [1, 2, 3]
y2 = [1, 8, 27]
plt.plot(x1, y1, x2, y2, 'ro-',  linewidth=4)
plt.axis([0, 6, 0, 100])
plt.xlabel("Number")
plt.ylabel('Squared & Cube number')
plt.legend()
plt.show()