from matplotlib import pyplot as plt

# Univariate plotting of data
# 1 Histogram
# 2 Density
# 2 Box & wisker tell us centraldetency of data outlier
import pandas
filename = 'indians-diabetes.data.csv'

hnames=['preg', 'plas','pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = pandas.read_csv(filename, names=hnames)
dataframe.plot(kind='box', subplots=True, layout=(3, 3), sharex=True )
plt.show()


# This is use to generate the report for remove the outlier.
