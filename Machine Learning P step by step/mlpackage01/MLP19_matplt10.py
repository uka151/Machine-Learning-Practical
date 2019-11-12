# Pie Chart
import matplotlib.pyplot as plt
labels = 'S1', 'S2', 'S3'
# label is type of tuple of array
Section =[30, 60, 10]
colors = ['r', 'g', 'b']
plt.pie(Section, labels=labels, colors=colors, startangle=90, explode=(0, 0.1, 0), autopct='%1.2f%%')

plt.title("Pie Chart")
plt.show()
