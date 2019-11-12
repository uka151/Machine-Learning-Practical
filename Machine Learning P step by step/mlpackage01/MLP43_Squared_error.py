# cross validation
import warnings
warnings.filterwarnings(action='ignore')
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

filename = 'housing.csv'
hnames = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

dataframe = pd.read_csv(filename, names=hnames)
array = dataframe.values
X = array[:, 0:13]
Y = array[:, 13]
kfold = KFold(n_splits=10)
model = LinearRegression()
scoringMethod = 'neg_mean_squared_error'   # MEA
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoringMethod)
print("Name : %.3f(%.3f)" % (results.mean(), results.std()))

# use the absolute value of all distance & then sum
# cost = error can say


