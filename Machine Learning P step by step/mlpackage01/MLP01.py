import csv
# load csv file with python standard library for knowledge purpose

filename = open('indians-diabetes.data.csv', 'r')
reader = csv.reader(filename, delimiter=',')
# list is a function that convert whole data into array

data = list(reader)

print(data)

for l in data:
    print(l)
print(" no of rows:", len(data))
