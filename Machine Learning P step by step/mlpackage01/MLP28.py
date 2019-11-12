# Rescale the data(Custom range b/w 1 to 5)
import pandas as pd
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler
filename = 'indians-diabetes.data.csv'
hnames=['preg', 'plas','pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(filename, names=hnames)

array = dataframe.values  # .value is a trick that data found  without meta data
# Separate the array into input & output components
X = array[:, 0:8]  # [rows, cols]
Y = array[:, 8]
scaler = MinMaxScaler(feature_range=(1,5))
# first Method
rescaledX = scaler.fit_transform(X)

# Summarize transformed data
set_printoptions(precision=2)
print(rescaledX[0:30, ])   # [rows, cols]