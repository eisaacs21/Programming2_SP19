# https://data.cityofchicago.org/Environment-Sustainable-Development/Chicago-Energy-Benchmarking/xq83-jr8c
import matplotlib.pyplot as plt
import csv
'''
Energy Efficiency of Chicago Schools (35pts)
Chicago requires that all buildings over 50000 square feet in the city comply with energy benchmark reporting each year.
We will use this data at the link above to look at schools.  
We will visualize the efficiency of schools by scatter plot.  
We hypothesize that the more square footage (sqft) a school is, the more greenhouse gas (ghg) emission it will produce.
An efficient school would have a large ratio of sqft to ghg.  
It would also be interesting to know where Parker lies on this graph???  Let's find out.
Make a scatterplot which does the following:  
- Plots the Total Greenhouse gas (GHG) Emmissions (y-axis), versus building square footage (x-axis) (13pts)
- Includes ONLY data for K-12 Schools. (3pts)
- Labelled x and y axis and appropriate title (3pt)
- Annotated labels (school name) for the 3 highest and 3 lowest GHG Intensities. (3pts)
- Label Francis W. Parker. (3pts)
- Create a best fit line for schools shown. (5pts)
- Customize your graph in a discernable way using any technique discussed or one from the API (matplotlib.org). (5pts)

Challenge (for fun if you have time... not required):
- Make schools in top 10 percent of GHG Intensity show in green.
- Make schools in bottom 10 percent GHG Intesity show in red.
- Add colleges and universities (use a different marker type)
'''
plt.figure(1)
with open('Notes\data\Chicago_Energy_Benchmarking.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
month_numbers = [x for x in range(12)]  # month numbers on x

library_names = [x[0] for x in data[1:]] # month names on x
print(library_names)

header = data.pop(0)
#print(header)

month_data = [x[1:-1] for x in data]  # Jan to Dec data for all libraries
print(month_data[0])

plt.figure(3, tight_layout=True, figsize=(12, 8))  # tight layout allows data to fit axes
'''
library_data = [int(x) for x in month_data[library_names.index('')]]
plt.bar(month_numbers, library_data)
plt.title("Energy Use")
plt.xlabel("Month")
plt.ylabel("Use")
'''
month_names = header[1:-1]
print(month_names)
plt.xticks(month_numbers, month_names, rotation=90, fontsize=8)  # replace number with labels


# Make a graph of all library attendance in Chicago by month
plt.figure(4, tight_layout=True, figsize=(6, 4), facecolor='lightblue')

print(month_data)

all_lib_months = [0 for x in range(12)]
print(all_lib_months)

for library in month_data:
    for i in range(12):
        all_lib_months[i] += int(library[i])

print(all_lib_months)

plt.bar(month_numbers, all_lib_months, color='red')
plt.xticks(month_numbers, month_names, rotation=90)
plt.xlabel("Months")
plt.ylabel("Use")
plt.title("Energy Use (2018)")


plt.show()