import warnings
warnings.filterwarnings(action='ignore')
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

filename = 'indians-diabetes.data.csv'
hnames=['preg', 'plas','pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(filename, names=hnames)
array = dataframe.values

X = array[:, 0:8]
Y = array[:, 8]
kfold = KFold(n_splits=10)

# 1) Spot Checking for Logistic Regression
#
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
results = cross_val_score(model, X, Y, cv=kfold)

print("Validation Score for Logistic Regression:", results.mean())

# 2) Spot Checking for Linear Discriminant Analysis (LDA)
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
model = LinearDiscriminantAnalysis()
results = cross_val_score(model, X, Y, cv=kfold)
print("Validation score for Linear Discriminant Analysis:", results.mean())

# 3) Spot Checking for K- Nearest Neighbors (KNN)
# always use the value of K equal to odd number like k= 3,5,7 etc

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier()
results = cross_val_score(model, X, Y, cv=kfold)
print("Validation score for KNeighbors :", results.mean())

# 4) Spot Checking for Gaussian Naive Bayes
# Application of Naive
# Multi class
# Real time prediction
# Text classification
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
results = cross_val_score(model, X, Y, cv=kfold)
print("Validation score for GaussianNB :", results.mean())

# 5) Classification and Regression Trees(Cart)/(Decision Tree
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
results = cross_val_score(model, X, Y, cv=kfold)
print("Validation score for Decision Tree :", results.mean())


# 6) Spot Checking for Support Vector Machine (SVM).
from sklearn.svm import SVC
model = SVC()
results = cross_val_score(model, X, Y, cv=kfold)
print("Validation score for SVM :", results.mean())
