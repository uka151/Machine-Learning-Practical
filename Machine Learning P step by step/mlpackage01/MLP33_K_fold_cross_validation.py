#  this technique is use maximum time & every data is use for training as well as testing data

from sklearn.model_selection import KFold
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
filename = 'indians-diabetes.data.csv'
hnames=['preg', 'plas','pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(filename, names=hnames)
array = dataframe.values
X = array[:, 0:8]
Y = array[:, 8]
model = LogisticRegression()
num_folds = 10
kfold = KFold(n_splits=num_folds)
results = cross_val_score(model, X, Y, cv=kfold)  # cv stand for cross validation
print("results :", results)
print("Accuracy:%.3f%%" % (results.mean() * 100.0))
print("Std.Deviation=%.3f" % (results.std() * 100.0))