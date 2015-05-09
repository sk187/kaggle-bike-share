Kaggle Bike Share Data
=================================
# Report:

## Purpose:
The purpose of this Kaggle Competition was to predict bike share demand based on whatever features you 
found helped. Demand was split into two categories, Causal users and registered users. The features 
provided were:

* Time Stamp
* Season (1: Winter, Spring: 2, Summer: 3, Fall: 4 )
* Holiday (1 or 0)
* Working Day (~Weekend & ~Holiday)
* Temp (in C)
* Atemp (What the weather felt like)
* Humidity (0 -100%)
* Casual
* Registered 
* Count (total)

## Created Columns:
* Avg Temp by Day (in F)
* Avg Temp by Week (in F)
* Daily Temp Deviation from Avg Weekly Temp
* Week Number by ISO
* Day of the Week (0-6 Mon - Sun)

## Hypothesis:

After doing some basic data visualization, I was convinced weather, both temperature and perception had a huge influence on demand. I wanted to better separate rain vs. snow, amount of precipitation (especially snow). I also saw that weekday vs weekends had a strong influence on bike demands for registered users but not necessary for casual riders. Finally registered ridership had a huge increase between the first and second year.   

## Modeling
I used Random Forest Models and was able to get a RMSE from Kaggle of 1.266. I played around with difference features for fitting the model but was not able to get a better score. However when I just used the information I was given (only splitting the time stamp), I was able to get a RMS of 0.46. 

## Ways to Improve
* Sunrise/ Sunset data
* Better categorizing Weather 
* Create dummy variables for days of the week

## Conclusion:
While the model is pretty good, it may not accurately model demand of registered riders as the popularity, availability and culture around bikes in DC changes. As seen with the huge shift between year 1 and 2 in the data for registered riders, there maybe continue to be a huge shift. It would be helpful to have total number of registered riders and then compare it to active ridership for any given hour. This would help make the model more accurate for this category. 