import pandas as pd
import numpy as np
import matplotlib.pylab as plt

####################
# Rentals by Month #
####################
# Registered 
df = pd.read_csv('/Users/sunggyunkim/Documents/Kaggle Bike Share/data/clean_data.csv')
df = df.drop(['Unnamed: 0'], axis=1)

month_registered_sum = df.groupby(['year', 'month']).registered.sum()
registered = month_registered_sum.values[0:12]
month = [1,2,3,4,5,6,7,8,9,10,11,12]

fig = plt.figure()
ax = plt.subplot(111)
ax.set_title('Registered Rental Numbers by Month')
ax.set_xlabel('Month')
ax.set_ylabel('# of Bikes Rented')
ax.bar(month, registered)
plt.savefig('/Users/sunggyunkim/Documents/Kaggle Bike Share/Charts/reg_bike_sum_by_month.png')

########################################################
# Casual 
month_casual_sum = df.groupby(['year','month']).casual.sum()
casual = month_casual_sum[0:12]
month = [1,2,3,4,5,6,7,8,9,10,11,12]

fig = plt.figure()
ax = plt.subplot(111)
ax.set_title('Casual Rental Numbers by Month')
ax.set_xlabel('Month')
ax.set_ylabel('# of Bikes Rented')
ax.bar(month, casual)
plt.savefig('/Users/sunggyunkim/Documents/Kaggle Bike Share/Charts/cas_bike_sum_by_month.png')

#####################
# Rental by Holiday #
#####################
rent_by_holiday_cas = df.groupby(['holiday']).casual.mean()
rent_by_holiday_reg = df.groupby(['holiday']).registered.mean()
fig = plt.figure()
ax = fig.add_subplot(111)

N = 2
cas_mean = rent_by_holiday_cas.values
reg_mean = rent_by_holiday_reg.values
ind = np.arange(N)
width = 0.35

rects1 = ax.bar(ind, cas_mean, width, color='blue')
rects2 = ax.bar(ind+width, reg_mean, width, color='red')

ax.set_title('Bike Rental Numbers On Holidays')
ax.set_ylabel('# of Bikes Rented')
xTickMarks = ['Not Holiday', 'Holiday']
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, fontsize=10)
plt.savefig('/Users/sunggyunkim/Documents/Kaggle Bike Share/Charts/Rent_on_Holidays.png')

#########################
# Rental by Temperature #
#########################
# Casual
temp = df.groupby(['temp_f']).casual.mean()
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Casual Bike Demand by Temperature')
ax.set_xlabel('# of Bikes Rented')
ax.set_ylabel('Temperature')
n = 49
ax.scatter(temp, temp.index)
plt.savefig('/Users/sunggyunkim/Documents/Kaggle Bike Share/Charts/Cas_Rent_by_Temp.png')

# Registered
temp = df.groupby(['temp_f']).registered.mean()
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Registered Bike Demand by Temperature')
ax.set_xlabel('# of Bikes Rented')
ax.set_ylabel('Temperature')
n = 49
ax.scatter(temp, temp.index)
plt.savefig('/Users/sunggyunkim/Documents/Kaggle Bike Share/Charts/Reg_Rent_by_Temp.png')

#####################
# Rental by Weather #
#####################
weather_cas = df.groupby(['weather']).casual.mean()
weather_reg = df.groupby(['weather']).registered.mean()

fig = plt.figure()
ax = fig.add_subplot(111)

N = 4
cas_mean = weather_cas.values
reg_mean = weather_reg.values
ind = np.arange(N)
width = 0.35

rects1 = ax.bar(ind, cas_mean, width, color='blue')
rects2 = ax.bar(ind+width, reg_mean, width, color='red')

fig.suptitle('Bike Rental By Weather Category')
ax.set_ylabel('# of Bikes Rented')
xTickMarks = [1,2,3,4]
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, fontsize=10)
ax.legend((rects1[0], rects2[0]), ('Casual', 'Registered'), loc=3,
          ncol=2, mode="expand", borderaxespad=0.)
plt.savefig('/Users/sunggyunkim/Documents/Kaggle Bike Share/Charts/Rent_by_weather.png')

########################
# Rental by Wind Speed #
########################
wind_cas = df.groupby(['windspeed']).casual.mean()
wind_reg = df.groupby(['windspeed']).registered.mean()

fig = plt.figure()
ax = fig.add_subplot(111)

N = 28
cas_mean = wind_cas.values
reg_mean = wind_reg.values
ind = np.arange(N)
width = 0.3

rects1 = ax.bar(ind, cas_mean, color='blue')
rects2 = ax.bar(ind+width, reg_mean, width, color='red')

fig.suptitle('Bike Rental By Wind Speed')
ax.set_ylabel('# of Bikes Rented')
ax.set_xticks(ind+width)
ax.legend((rects1[0], rects2[0]), ('Casual', 'Registered'), loc=3,
          ncol=2, mode="expand", borderaxespad=0.)

##################
# Rental by Hour #
##################
hour_cas = df.groupby(['hour']).casual.mean()
hour_reg = df.groupby(['hour']).registered.mean()

fig = plt.figure()
ax = fig.add_subplot(111)

N = 24
cas_mean = hour_cas.values
reg_mean = hour_reg.values
ind = np.arange(N)
width = 0.35

rects1 = ax.bar(ind, cas_mean, width, color='blue')
rects2 = ax.bar(ind+width, reg_mean, width, color='red')

fig.suptitle('Bike Rental By Hour')
ax.set_ylabel('# of Bikes Rented')
ax.set_xticks(ind+width)
xTickMarks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, fontsize=10)
ax.legend((rects1[0], rects2[0]), ('Casual', 'Registered'), loc=3,
          ncol=2, mode="expand", borderaxespad=0.)
plt.savefig('/Users/sunggyunkim/Documents/Kaggle Bike Share/Charts/Rent_by_hour.png')

#####################
# Rental by weekday #
#####################

cas = df.groupby(['weekday']).casual.mean()
reg = df.groupby(['weekday']).registered.mean()

fig = plt.figure()
ax = fig.add_subplot(111)

N = 7
cas_mean = cas.values
reg_mean = reg.values
ind = np.arange(N)
width = 0.35

rects1 = ax.bar(ind, cas, width, color='blue')
rects2 = ax.bar(ind+width, reg, width, color='red')

fig.suptitle('Bike Rental By Weekday')
ax.set_ylabel('# of Bikes Rented')
ax.set_xticks(ind+width)
xTickMarks = ['M','T','W','Th','F','Sat', 'Sun']
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, fontsize=10)
ax.legend((rects1[0], rects2[0]), ('Casual', 'Registered'), loc=3,
          ncol=2, mode="expand", borderaxespad=0.)
plt.savefig('/Users/sunggyunkim/Documents/Kaggle Bike Share/Charts/Rent_by_day_of_week.png')


####################
# Rental by Season #
####################

cas = df.groupby(['season']).casual.mean()
reg = df.groupby(['season']).registered.mean()

fig = plt.figure()
ax = fig.add_subplot(111)

N = 4
cas_mean = cas.values
reg_mean = reg.values
ind = np.arange(N)
width = 0.35

rects1 = ax.bar(ind, cas, width, color='blue')
rects2 = ax.bar(ind+width, reg, width, color='red')

fig.suptitle('Bike Rental By Season')
ax.set_ylabel('# of Bikes Rented')
ax.set_xticks(ind+width)
xTickMarks = ['Winter','Spring','Summer','Fall']
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, fontsize=10)
ax.legend((rects1[0], rects2[0]), ('Casual', 'Registered'), loc=3,
          ncol=2, mode="expand", borderaxespad=0.)
plt.savefig('/Users/sunggyunkim/Documents/Kaggle Bike Share/Charts/Rent_by_season.png')


cols = ['casual','temp_f','hour', 'season']
df[cols]

######################
# Rental by Humidity #
######################

cas = df.groupby(['humidity']).casual.mean()
reg = df.groupby(['humidity']).registered.mean()

fig = plt.figure()
ax = fig.add_subplot(111)

N = 89
cas_mean = cas.values
reg_mean = reg.values
ind = np.arange(N)
width = 0.35

rects1 = ax.bar(ind, cas_mean, width, color='blue')
rects2 = ax.bar(ind+width, reg_mean, width, color='red')

fig.suptitle('Bike Rental By Humidity')
ax.set_ylabel('# of Bikes Rented')
ax.set_xticks(ind+width)
plt.setp(xtickNames, fontsize=10)
ax.legend((rects1[0], rects2[0]), ('Casual', 'Registered'), loc=3,
          ncol=2, mode="expand", borderaxespad=0.)
plt.savefig('/Users/sunggyunkim/Documents/Kaggle Bike Share/Charts/Rent_by_humidity.png')

#############################
# Charts from Train_Predict #
#############################

# Predicted vs Actual Scatter Plot
fig = plt.figure()
ax.scatter(y_test, y_test, c="blue")
ax.scatter(y_test, predict_casual, c="red")
ax.set_xlabel('Actual Value')
ax.set_ylabel('Predicted Value')
ax.set_title('Actual Vs Predicted Bike Rental')
plt.savefig('/Users/sunggyunkim/Documents/Kaggle Bike Share/Charts/Actual_vs_Prediction_Scatter_Casual.png')

# Residual Scatter Plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(y_test, y_test-predict_casual)
ax.set_xlabel('Actual Value')
ax.set_ylabel('Predicted Value')
ax.set_title('Residuals for Casual')
plt.savefig('/Users/sunggyunkim/Documents/Kaggle Bike Share/Charts/Actual_vs_Prediction_Scatter_Residuals.png')


