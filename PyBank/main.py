
#Create variables
total_months = 0
total_amount = 0
average_change = 0
greatest_increase_month = ""
greatest_increase_amount = 0
greatest_decrease_month = ""
greatest_decrease_amount = 0

#Import operating system module
import os

#Import module for reading CSV files
import csv

#Create path to CSV file
csvpath = os.path.join('Resources', 'budget_data.csv')

#Open CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


#Loop through rows in CSV file
for row in csvreader:
    #Count total months
    total_months += 1
    #Calculate total amount
    total_amount += int(row[1])
    #Calculate average change
    average_change = total_amount / total_months
    #Calculate greatest increase in profits
    if int(row[1]) > greatest_increase_amount:
        greatest_increase_amount = int(row[1])
        greatest_increase_month = row[0]
    #Calculate greatest decrease in profits
    if int(row[1]) < greatest_decrease_amount:
        greatest_decrease_amount = int(row[1])
        greatest_decrease_month = row[0]

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_amount))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + str(greatest_increase_month) + " ($" + str(greatest_increase_amount) + ")")
print("Greatest Decrease in Profits: " + str(greatest_decrease_month) + " ($" + str(greatest_decrease_amount) + ")")
