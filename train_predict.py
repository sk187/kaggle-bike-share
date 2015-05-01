import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import sklearn
from sklearn import tree 
from sklearn.cross_validation import train_test_split
from sklearn import ensemble
from sklearn.metrics import mean_squared_error as mse


x_data = pd.read_csv('/Users/sunggyunkim/Documents/Kaggle Bike Share/clean_data.csv')
y_data = pd.read_csv('/Users/sunggyunkim/Documents/Kaggle Bike Share/clean_data.csv')
train_data = pd.read_csv('/Users/sunggyunkim/Documents/Kaggle Bike Share/clean_data.csv')

#####################################################################################################
# Decision Tree Modeling 
#####################################################################################################
train, test = train_test_split(train_data,test_size=0.3, random_state=1)

# Convert back to DF
train = pd.DataFrame(data=train, columns=train_data.columns)
test = pd.DataFrame(data=test, columns=train_data.columns)

#Creates list of column names
features = train_data.columns.tolist()[1:]

# Create DTC
ctree = tree.DecisionTreeClassifier(random_state=1)
# Fit Data
ctree.fit(train.drop('casual', axis=1), train['casual'])

# Shows feature discrimination metric
ctree.feature_importances_
pd.DataFrame(zip(features, ctree.feature_importances_)).sort_index(by=1, ascending=False)

#####################################################################################################
# Random Forest Modeling 
#####################################################################################################

##########
# Casual #
##########
x = x_data
x = x_data.drop(['Unnamed: 0'], axis=1)
y = y_data.drop(['Unnamed: 0'], axis=1)

cols = ['season','holiday','workingday','weather','temp_f',
        'd_low','hour', 'month', 'weekday','wavg_to_davg_temp_diff',
        'd_high', 'd_avg', 'atemp','casual']

rf = ensemble.RandomForestRegressor(n_estimators =200)
x_train, x_test, y_train, y_test = train_test_split(x[cols], y.casual, random_state=1)

# Fit Model
rf.fit (x_train, y_train)

# Score Model
rf.score (x_test, y_test) # R^2 of 0.93082716777487673 

# Predict X values of Test
predict_casual = rf.predict(x_test)

# Calculate Mean Score Error
MSE = mse(y_test, predict_casual) # Mean Square Error 185.69180926708304

# Calculate Root Mean Score Error
RMSE = mse(y_test, predict_casual)**0.5 # Root Mean Square Error of 13.626878192274379

# See Feature Significance 
features = x[cols].columns.tolist()[1:]
pd.DataFrame(zip(features, rf.feature_importances_)).sort_index(by=1, ascending=False)
# 6                    month  0.360050
# 2                  weather  0.137337
# 4                    d_low  0.074306
# 9                   d_high  0.067808
# 8   wavg_to_davg_temp_diff  0.059841
# 11                   atemp  0.028270
# 3                   temp_f  0.019789
# 5                     hour  0.017343
# 10                   d_avg  0.015457
# 7                  weekday  0.014989
# 0                  holiday  0.004516
# 1               workingday  0.002624

##############
# Registered #
##############
x = x_data
x = x_data.drop(['registered','Unnamed: 0'], axis=1)
y = y_data.drop(['Unnamed: 0'], axis=1)

cols = ['season','holiday','workingday','weather','temp_f',
        'd_low','hour', 'month', 'weekday','wavg_to_davg_temp_diff',
        'd_high', 'd_avg', 'atemp']
rf = ensemble.RandomForestRegressor(n_estimators =200)

x_train, x_test, y_train, y_test = train_test_split(x[cols], y.registered, random_state=1)
rf.fit (x_train, y_train)
rf.score (x_test, y_test) # R^2 of 0.94023364147558819 

predict_registered = rf.predict(x_test)

MSE = mse(y_test, predict_registered) # 1378.5795422299777
RMSE = mse(y_test, predict_registered)**0.5 # 37.129227600772651

# See Feature Significance 
features = x[cols].columns.tolist()[1:]
pd.DataFrame(zip(features, rf.feature_importances_)).sort_index(by=1, ascending=False)
# 6                    month  0.560085
# 2                  weather  0.121247
# 9                   d_high  0.071061
# 11                   atemp  0.050054
# 7                  weekday  0.041380
# 8   wavg_to_davg_temp_diff  0.028708
# 4                    d_low  0.024742
# 3                   temp_f  0.022625
# 10                   d_avg  0.021412
# 5                     hour  0.020346
# 0                  holiday  0.008552
# 1               workingday  0.000974

