import matplotlib.pyplot as plt
plt.figure(1)
plt.title("Easy number 1, 2, 3")
plt.axis([0, 5, 0, 30])
plt.subplot(311)
plt.plot([1, 2, 3])
plt.subplot(312)
plt.plot([1, 4, 9])

plt.subplot(313)
plt.plot([1, 8, 27])
plt.show()