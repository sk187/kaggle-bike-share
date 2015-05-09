import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn import ensemble

train_data = pd.read_csv('/Users/sunggyunkim/Documents/Kaggle Bike Share/data/clean_data.csv')
train_data = train_data.drop(['Unnamed: 0'], axis=1)
test_data = pd.read_csv('/Users/sunggyunkim/Documents/Kaggle Bike Share/data/clean_test_data.csv')
test_data = test_data.drop(['Unnamed: 0'], axis=1)
##########
# Casual #
##########
cols = ['season','holiday','workingday','weather','temp_f',
        'd_low','hour', 'month', 'weekday','wavg_to_davg_temp_diff',
        'd_high', 'd_avg', 'atemp']

rf = ensemble.RandomForestRegressor(n_estimators =200)

rf.fit (train_data[cols], train_data.casual)
predict_casual = rf.predict(test_data[cols])

##############
# Registered #
##############
cols = ['season','holiday','workingday','weather','temp_f',
        'd_low','hour', 'month', 'weekday','wavg_to_davg_temp_diff',
        'd_high', 'd_avg', 'atemp']
rf = ensemble.RandomForestRegressor(n_estimators =200)
x_train, x_test, y_train, y_test = train_test_split(train_data[cols], train_data.registered, random_state=1)

rf.fit (train_data[cols], train_data.casual)
predict_registered = rf.predict(test_data[cols])

##############
# Submission #
##############

count = [int(round(i+j)) for i,j in zip(predict_casual, predict_registered)]
df_submission = pd.DataFrame(count, test_data.datetime, columns = ['count'])
pd.DataFrame.to_csv(df_submission, '/Users/sunggyunkim/Documents/Kaggle Bike Share/data/randomforest_predict.csv')


####################################################################################################
#############
# 2nd Model #
#############
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn import ensemble

train_data = pd.read_csv('/Users/sunggyunkim/Documents/Kaggle Bike Share/data/clean_data.csv')
train_data = train_data.drop(['Unnamed: 0'], axis=1)
test_data = pd.read_csv('/Users/sunggyunkim/Documents/Kaggle Bike Share/data/clean_test_data.csv')
test_data = test_data.drop(['Unnamed: 0'], axis=1)
##########
# Casual #
##########
cols = ['season','weather','temp_f','hour', 'month', 'weekday','atemp']

rf = ensemble.RandomForestRegressor(n_estimators =200)

rf.fit (train_data[cols], train_data.casual)
predict_casual = rf.predict(test_data[cols])

##############
# Registered #
##############
cols = ['season','weather','temp_f','hour', 'month', 'weekday','atemp']
rf = ensemble.RandomForestRegressor(n_estimators =200)
x_train, x_test, y_train, y_test = train_test_split(train_data[cols], train_data.registered, random_state=1)

rf.fit (train_data[cols], train_data.casual)
predict_registered = rf.predict(test_data[cols])

##############
# Submission #
##############

count = [int(round(i+j)) for i,j in zip(predict_casual, predict_registered)]
df_submission = pd.DataFrame(count, test_data.datetime, columns = ['count'])
pd.DataFrame.to_csv(df_submission, '/Users/sunggyunkim/Documents/Kaggle Bike Share/data/randomforest_predict2.csv')

####################################################################################################
#############
# 3nd Model #
#############
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn import ensemble

train_data = pd.read_csv('/Users/sunggyunkim/Documents/Kaggle Bike Share/data/clean_data.csv')
train_data = train_data.drop(['Unnamed: 0'], axis=1)
test_data = pd.read_csv('/Users/sunggyunkim/Documents/Kaggle Bike Share/data/clean_test_data.csv')
test_data = test_data.drop(['Unnamed: 0'], axis=1)
##########
# Casual #
##########
cols = ['season','holiday','workingday','weather','temp_f',
        'd_low','hour', 'month', 'weekday','wavg_to_davg_temp_diff',
        'd_high', 'd_avg', 'atemp']
rf = ensemble.RandomForestRegressor(n_estimators =1000, min_samples_split=6, oob_score=True)

rf.fit (train_data[cols], train_data.casual)
predict_casual = rf.predict(test_data[cols])

##############
# Registered #
##############
cols = ['season','holiday','workingday','weather','temp_f',
        'd_low','hour', 'month', 'weekday','wavg_to_davg_temp_diff',
        'd_high', 'd_avg', 'atemp']
rf = ensemble.RandomForestRegressor(n_estimators =1000, min_samples_split=6, oob_score=True)
x_train, x_test, y_train, y_test = train_test_split(train_data[cols], train_data.registered, random_state=1)

rf.fit (train_data[cols], train_data.casual)
predict_registered = rf.predict(test_data[cols])

##############
# Submission #
##############

count = [int(round(i+j)) for i,j in zip(predict_casual, predict_registered)]
df_submission = pd.DataFrame(count, test_data.datetime, columns = ['count'])
pd.DataFrame.to_csv(df_submission, '/Users/sunggyunkim/Documents/Kaggle Bike Share/data/randomforest_predict3.csv')

####################################################################################################
#############
# 4nd Model #
#############
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn import ensemble

train_data = pd.read_csv('/Users/sunggyunkim/Documents/Kaggle Bike Share/data/clean_data.csv')
train_data = train_data.drop(['Unnamed: 0'], axis=1)
test_data = pd.read_csv('/Users/sunggyunkim/Documents/Kaggle Bike Share/data/clean_test_data.csv')
test_data = test_data.drop(['Unnamed: 0'], axis=1)
##########
# Casual #
##########
cols = ['season','weather','temp_f','hour', 'month', 'weekday','atemp']        

rf = ensemble.RandomForestRegressor(n_estimators =1000, min_samples_split=6, oob_score=True)

rf.fit (train_data[cols], train_data.casual)
predict_casual = rf.predict(test_data[cols])

##############
# Registered #
##############
cols = ['season','weather','temp_f','hour', 'month', 'weekday','atemp']        

rf = ensemble.RandomForestRegressor(n_estimators =1000, min_samples_split=6, oob_score=True)
x_train, x_test, y_train, y_test = train_test_split(train_data[cols], train_data.registered, random_state=1)

rf.fit (train_data[cols], train_data.casual)
predict_registered = rf.predict(test_data[cols])

##############
# Submission #
##############

count = [int(round(i+j)) for i,j in zip(predict_casual, predict_registered)]
df_submission = pd.DataFrame(count, test_data.datetime, columns = ['count'])
pd.DataFrame.to_csv(df_submission, '/Users/sunggyunkim/Documents/Kaggle Bike Share/data/randomforest_predict4.csv')

####################################################################################################

