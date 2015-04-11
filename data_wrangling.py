import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import sklearn
from sklearn.cross_validation import train_test_split
from sklearn import ensemble

df = pd.read_csv('/Users/sunggyunkim/Documents/Kaggle Bike Share/train.csv')

# Parsing long_datetime into long_date and time
hour = []
year = []
month = []
day = []
for date in df.datetime:

    # Spliting datetime into date and time
    a = date.split(' ')
    # Spliting Dates by -
    b = a[0].split('-')
    year.append(int(b[0]))
    month.append(int(b[1]))
    day.append(int(b[2]))
    # Spliting Time by :
    c = a[1].split(":")
    hour.append(int(c[0]))
# Add new columns

df['hour'] = pd.Series(hour)
df['year'] = pd.Series(year)
df['month'] = pd.Series(month)
df['day'] = pd.Series(day)

# Drop Datetime Column
df = df.drop(['datetime'], axis=1)

X = df.values
y = df['casual'].values
X = np.delete(X, 9, axis=1)

# Add Days of the Week ['Sat', 'Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri']
days_of_the_week = [0,1,2,3,4,5,6]
days_in_data = []

num = 0
i = 0
while i < 10886:
    if num > 6:
        num = 0
    days_in_data.append(days_of_the_week[num])
    num += 1
    i += 1
df['day_of_week'] = days_in_data



# Machine Learning Models
# __________________________________________________________________________

# Creating Train and Test Models
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=0)

# RandomForest
clf = ensemble.RandomForestClassifier(n_estimators=50)
clf.fit(X_train, y_train)
clf.score(X_test, y_test)  # Getting about 0.5

# GradientBoosting Currently not working
clf = ensemble.GradientBoostingClassifier(n_estimators=50)
clf.fit(X_train, y_train)
clf.score(X_test, y_test)

X = np.delete(X, 10, axis=1)


# Charts Tables
# _______________________________________________________________________

labels = ['Winter', 'Fall', 'Summer', 'Spring']
sizes = df.season.value_counts()
size_labeles = []
size_num = []

for key in sizes.keys():
    size_labeles.append(key)

for value in sizes:
    size_num.append(value)

# Creates Num of Rental Days by Season Pie Chart
fig = plt.figure()
fig.suptitle("Days of Rental by Season")
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
plt.pie(sizes, autopct='%1.1f%%', labels = labels)
plt.show()
