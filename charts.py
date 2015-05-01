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

# Create Rentals by Day of the Week
days = []
bike_count = []

for day in df['day_of_the_week'] :
    days.append(day)
for num in df.count :
    bike_count.append(num)

fig = plt.figure()
plt.title('Rentals by Day of the Week')
plt.bar(days, bike_count, width=100)