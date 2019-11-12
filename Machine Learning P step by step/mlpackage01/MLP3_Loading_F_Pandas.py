# Load CSV file using Pandas offline & online
import pandas as pd
filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(filename, names= hnames)
# get the information about data
print(dataframe.shape)
print(dataframe)
print(dataframe.head(5))
print(dataframe.describe())
print(dataframe.sample(5))
print(dataframe.groupby('class').size())
print(dataframe)

# Online data read
import urllib.request
web_path = urllib.request.urlopen('https://goo.gl/QnHW4g')
hnms=['sepal-length','sepal-width','petal-length','petal-width','class']
df = pd.read_csv(web_path, names=hnms)
print(df)
print(df.shape)
print(df.sample(5))
print(df.groupby('class').size())
print(df.columns)
