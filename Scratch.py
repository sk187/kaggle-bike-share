labels = ['Winter', 'Fall', 'Summer', 'Spring']
sizes = df.season.value_counts()
size_labeles = []
size_num = []

for key in sizes.keys():
    size_labeles.append(key)

for value in sizes:
    size_num.append(value)

fig = plt.figure()
fig.suptitle("Days of Rental by Season")
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
# ax.set_title('axes title')
# ax.set_xlabel('xlabel')
# ax.set_ylabel('ylabel')
plt.pie(sizes, autopct = '%1.1f%%', labels = labels)
plt.show()

# Creates Num of Rental Days by Season
fig = plt.figure()
fig.suptitle("Days of Rental by Season")
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
plt.pie(sizes, autopct='%1.1f%%', labels = labels)
plt.show()
