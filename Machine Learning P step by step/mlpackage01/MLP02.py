import numpy as np

filename = 'indians-diabetes.data.csv'
raw_data = open(filename, 'r')
data = np.loadtxt(raw_data, delimiter=',')

print(data)

for l in data:
    print(l)
print(data.shape)
print(data.size)
