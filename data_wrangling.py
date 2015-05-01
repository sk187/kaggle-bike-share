import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import sklearn
from sklearn.cross_validation import train_test_split
from sklearn import ensemble
import datetime

df = pd.read_csv('/Users/sunggyunkim/Documents/Kaggle Bike Share/train.csv')
# df = pd.read_csv('/Users/sunggyunkim/Documents/Kaggle Bike Share/test.csv')

def get_weekday(year, month, day):
    return datetime.date(year, month, day).weekday()

def get_iso_week_num(year, month, day):
    return datetime.date(year, month, day).isocalendar()[1]

def get_day_temp_high(year, month, day):
    return df[(df.year == year) & (df.month == month) & (df.day == day)].temp_f.max()

def get_day_temp_low(year, month, day):
    return df[(df.year == year) & (df.month == month) & (df.day == day)].temp_f.min()

def get_day_temp_avg(year, month, day):
    return df[(df.year == year) & (df.month == month) & (df.day == day)].temp_f.mean()

def get_week_temp_avg(day, month, year, week_num):
    return df[(df.year == year) & (df.month == month) & (df.day == day) & (df.week_num == week_num) & (df.year == year)].temp_f.mean()

# Parsing long_datetime into long_date and time
hour = []
year = []
month = []
day = []
weekday = []
iso_week_num = []

for date in df.datetime:
    # Spliting datetime into date and time
    a = date.split(' ')
    # Spliting Dates by -
    b = a[0].split('-')
    y = int(b[0])
    m = int(b[1])
    d = int(b[2])
    # Get Weekday ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'] (0-6)
    week_day = get_weekday(y,m,d)
    # Get ISO Week Number
    week_num = get_iso_week_num(y,m,d)
    # Append info to array
    year.append(y)
    month.append(m)
    day.append(d)
    weekday.append(week_day)
    iso_week_num.append(week_num)
    # Spliting Time by :
    c = a[1].split(":")
    hour.append(int(c[0]))
       
# Add new columns
df['hour'] = hour
df['year'] = year
df['month'] = month
df['day'] = day
df['weekday'] = weekday
df['week_num'] = iso_week_num

# Convert C to F
temp_f = []
for temp in df.temp:
    f = temp * 9/5 +32
    formatted_f = float("{0:.0f}".format(f))
    temp_f.append(formatted_f)  
df['temp_f'] = temp_f

# Add Temp columns
day_temp_low = []
day_temp_high = []
day_temp_avg = []
week_temp_avg = []
day_vs_week_temp_difference = []

for index in df.index:
    y = df[df.index == index].year.iloc[0]
    m = df[df.index == index].month.iloc[0]
    d = df[df.index == index].day.iloc[0]
    temp = df[df.index == index].temp.iloc[0]
    week_num = df[df.index == index].week_num.iloc[0]
    # Get Daily Temp High
    d_high = get_day_temp_high(y,m,d)
    # Get Daily Temp Low
    d_low = get_day_temp_low(y,m,d)
    # Get Daily Avg
    d_avg = get_day_temp_avg(y,m,d)
    # Get Week Temp Avg
    week_avg = get_week_temp_avg(y, week_num)
    # Difference Between Weekly Avg And Daily Avg
    diff = week_avg - d_avg
    # Append info to array
    day_temp_low.append(d_high)
    day_temp_high.append(d_low)
    day_temp_avg.append(d_avg)
    week_temp_avg.append(week_avg)
    day_vs_week_temp_difference.append(diff)
df['d_low'] = day_temp_low
df['d_high'] = day_temp_high
df['d_avg'] = day_temp_avg
df['w_avg'] = week_temp_avg
df['wavg_to_davg_temp_diff'] = day_vs_week_temp_difference


# Drop Datetime Column
df = df.drop(['datetime'], axis=1)
X = df.values
y = df['casual'].values
X = np.delete(X, 9, axis=1)

df.to_csv('/Users/sunggyunkim/Documents/Kaggle Bike Share/clean_data.csv')