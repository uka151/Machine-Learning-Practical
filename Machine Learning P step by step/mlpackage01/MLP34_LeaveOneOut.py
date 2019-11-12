# this is specialized version of Kfold
# in this number of training instance = number of group may be
# hide only one row & use all the training instance for model develope & apply for test with help of hiding row

import warnings
warnings.filterwarnings(action='ignore')
from pandas import read_csv
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
filename = 'indians-diabetes.data.csv'
hnames=['preg', 'plas','pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=hnames)
array = dataframe.values
X = array[:, 0:8]
Y = array[:, 8]
loocv = LeaveOneOut()
model = LogisticRegression()
results = cross_val_score(model, X, Y, cv=loocv)
print("Results:", results)
print("Results.size:", results.size)
print("Sum of Positive Results :%i" % (results.sum()))
print("Accuracy=0.2ff%%" %(results.sum() *100/results.size))