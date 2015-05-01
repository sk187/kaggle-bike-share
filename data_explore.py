import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import sklearn
from sklearn.cross_validation import train_test_split
from sklearn import ensemble
df = pd.read_csv('/Users/sunggyunkim/Documents/Kaggle Bike Share/clean_data.csv')

df.groupby('workingday').workingday.count()
# workingday
# 0             3474
# 1             7412

df.groupby('month').temp.mean()
# 1         9.840000
# 2        11.798535
# 3        15.902175
# 4        18.718372
# 5        22.674079
# 6        27.064496
# 7        30.841711
# 8        29.736689
# 9        25.779032
# 10       20.933853
# 11       15.185752
# 12       13.831206

df.groupby('month').temp_f.mean()
# month
# 1        49.720588
# 2        53.276360
# 3        60.642619
# 4        65.713971
# 5        72.744518
# 6        80.733553
# 7        87.585526
# 8        85.601974
# 9        78.427943
# 10       69.669594
# 11       59.411636
# 12       56.969298

df.groupby(['month']).casual.mean()
# month
# 1         8.203620
# 2        10.318535
# 3        27.809101
# 4        43.798680
# 5        45.268640
# 6        53.260965
# 7        55.862939
# 8        50.296053
# 9        50.496150
# 10       41.807903
# 11       27.829857
# 12       16.118421

df.groupby(['month']).registered.mean()
# month
# 1         82.162896
# 2         99.684795
# 3        120.360710
# 4        140.361936
# 5        174.190789
# 6        188.770833
# 7        179.462719
# 8        183.822368
# 9        183.309131
# 10       185.891328
# 11       165.847420
# 12       159.495614

df.groupby(['weekday']).registered.mean()
# weekday
# 0          160.546744
# 1          166.744639
# 2          165.889749
# 3          173.289118
# 4          166.842381
# 5          133.040404
# 6          123.788474

df.groupby(['weekday']).casual.mean()
# weekday
# 0          29.843972
# 1          22.979207
# 2          22.521599
# 3          24.007083
# 4          31.001962
# 5          63.625000
# 6          57.051298

df['temp_f'].describe()
# count    10886.000000
# mean        68.444516
# std         14.027494
# min         33.000000
# 25%         57.000000
# 50%         69.000000
# 75%         79.000000
# max        106.000000
