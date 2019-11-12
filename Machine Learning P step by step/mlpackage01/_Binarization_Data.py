# Binarization
# convert the contigouse data into discrete data (cotegry data)
from sklearn.preprocessing import Binarizer
from pandas import read_csv
filename = 'indians-diabetes.data.csv'
hnames=['preg', 'plas','pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=hnames)
array = dataframe.values
# Separate array into input & output component
X = array[:, 0:8]
Y = array[:, 8]
binarizer = Binarizer(threshold=5)
# threshold 6 means all the value above 6 then convert value in 1 & less than to 0
binaryX = binarizer.fit_transform(X)
# summarize transformed data
print(binaryX[0:30, :])