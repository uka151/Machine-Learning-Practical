# Standardize the data
# Gaussian with zero mean & unit variance
from sklearn.preprocessing import StandardScaler
# Standardize  means is convert data  into normal distribution is called Gossian Distribution
from pandas import read_csv
from numpy import set_printoptions
import numpy as np
filename = 'indians-diabetes.data.csv'
hnames=['preg', 'plas','pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=hnames)
array = dataframe.values
# Separate array into input & output component
X = array[:, 0:8]
Y = array[:, 8]
scaler = StandardScaler()
rescaledX = scaler.fit_transform(X)
print(rescaledX[:30, :])

print("\n\n Means of first Coloum =")
print(np.mean(rescaledX[:, 0]))



