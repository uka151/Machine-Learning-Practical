import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y, marker='o', markerfacecolor='red', markersize=15, linestyle='dashed', color='blue' )
plt.title("No of Square represent")
plt.xlabel("Natural Number", fontsize=10, color='red')
plt.ylabel("Squared Number", fontsize=10, color='green')
plt.axis([0, 6, 0, 26])
plt.annotate('Square of 5', xytext=(4.5,28), xy=(5, 25),arrowprops=dict(facecolor='black', shrink= 1))
plt.show()