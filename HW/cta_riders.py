# CTA Ridership (28pts)

#  Get the csv from the following data set.
#  https://data.cityofchicago.org/Transportation/CTA-Ridership-Annual-Boarding-Totals/w8km-9pzd
#  This shows CTA ridership by year going back to the 80s
import matplotlib as plt
import csv

with open('CTA_-_Ridership_-_Annual_Boarding_Totals.csv') as f:
    reader = csv.reader(f)  # create a reader object from csv lib
    data = list(reader)  # cast it as a list
print(data)

month_numbers = [x for x in range(12)]  # month numbers on x

library_names = [x[0] for x in data[1:]] # month names on x
print(library_names)

header = data.pop(0)
#print(header)

month_data = [x[1:-1] for x in data]  # Jan to Dec data for all libraries
print(month_data[0])

plt.figure(3, tight_layout=True, figsize=(100, 10))  # tight layout allows data to fit axes

library_data = [int(x) for x in month_data[library_names.index('Lincoln Park')]]
plt.bar(month_numbers, library_data)
plt.title("CTA BUS -Riders by Year")
plt.xlabel("Year")
plt.ylabel("Riders")

month_names = header[1:-1]
print(month_names)
plt.xticks(month_numbers, month_names, rotation=90, fontsize=8)

#1  Make a plot of rail usage for the most current 10 year period.  (year on x axis, and ridership on y) (5pts)
#2  Plot bus usage for the same years as a second line on your graph. (5pts)
#3  Plot bus and rail usage together on a third line on your graph. (5pts)
#4  Add a title and label your axes. (5pts)
#5  Add a legend to show data represented by each of the three lines. (5pts)
#6  What trend or trends do you see in the data?  Offer at least two hypotheses which might explain the trend(s). (3pts)