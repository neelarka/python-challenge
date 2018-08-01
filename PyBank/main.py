import os
import csv
from pathlib import Path  
filepath = Path("../../Desktop/budget_data.csv")
with open(filepath, newline="", encoding='utf-8' ) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    reader = csv.reader(csvfile)
    next(reader, None)
    date = []
    revenue = []
    for row in csvreader:
                date.append(row[0])
                revenue.append(int(row[1]))

    #print(date)
    #print(revenue)
length = len(date)
print("Financial Analysis" + "\n --------------------")
print ("The Total months : " + str(length))
total = 0
for x in revenue :
    total = total + x
print("Total : "  + str(total))

# Calculating Average change
change = []
x = 0
for number in revenue :
    if x<85 :
        change.append(revenue[x+1] - revenue[x])
        x = x+1
#print(change)
total1 = 0
for y in change :
    total1 = total1 + y
#print(total1)
average_change = total1/(length - 1)
print("The average change : " + str("%.2f" % average_change))

# Greatest Increase in Profit

Greatest_Increase = max(change)
index_max = (change.index(max(change)) + 1)
greatest_increase_date = (date[index_max])
print("The Greatest Decrease in Profits " + greatest_increase_date  + " (" + str(Greatest_Increase) + ")" )

# Greatest Decrease in Profit

Greatest_Decrease = min(change)
index_min = (change.index(min(change)) + 1)
greatest_decrease_date = (date[index_min])
print("The Greatest Decrease in Profits " + greatest_decrease_date  + " (" + str(Greatest_Decrease) + ")" )
