from matplotlib import pyplot as plt
import pandas
filename = 'indians-diabetes.data.csv'

hnames=['preg', 'plas','pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = pandas.read_csv(filename, names=hnames)
dataframe.plot(kind='density', subplots=True, layout=(3, 3), sharex=True )
plt.show()