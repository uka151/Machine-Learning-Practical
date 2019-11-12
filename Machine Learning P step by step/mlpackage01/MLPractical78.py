import numpy as np
import pandas as pd
s = pd.Series([1, 3, np.nan, 15, 7, 8])

print(s)

# When print the report  of any pandas data then its print by defualt data with Meta data
# 1 dinmension = Series = Vector in ML
dates = pd.date_range('20190101', periods=6, freq="D")
print(dates)

dates = pd.date_range('20190101', periods=6, freq="M")
print(dates)
dates = pd.date_range('20190101', periods=6, freq="Y")
print(dates)



print( np.random.randn(6, 4)) # X Genarate Matrix 6*4 with random value
# Dataframe = Excel example(Data, Row heading , Column heading)
# In ML we can not use the rows heading we use only index for rows heading & use for columns heading same its name
df = pd.DataFrame(np.random.rand(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)
print("Heading in Dataframe :", df.columns)
print("Row Heading in Dataframe :", df.index)
print("Values in Dataframe :", df.values)

df['E'] = df['A'].apply(lambda x: 1 if(x > 0) else 0)
# Features engineering df['E'] we can add new columns in the data called features engineering
print(df)

df['F'] = df['B'].apply(lambda x: 10 if(x > 2) else 0)

print(df)

print(df.dtypes)

# we cant use directly the column of string contain(object) in ML if want to use this column then convert into numeric

print(df.head())
print(df.tail(3))
print(df.sample(3))  # choose randomly 3 number and print , by default its print only one data

# most important topic which decided way of coding. it is first & bigest milstone

print(df.describe())

# describe never give the report of object by defualt & if want to finid report of object (string) then use following technique

print(df.describe(include="all"))

# Sorting by values

print("orginal values : \n", df)

print("sorted values :\n")
print(df.sort_values(by ='B', ascending=True))

# if want to delete any column then use del keyword

del df["F"]
print(df)

print(df.groupby('E').size())