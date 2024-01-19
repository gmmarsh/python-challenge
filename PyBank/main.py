#Import modules
import os
import csv

#Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

#Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #Create variables
    total_months = 0
    total_amount = 0
    average_change = 0
    greatest_increase_amount = 0
    greatest_increase_month = ""
    greatest_decrease_amount = 0
    greatest_decrease_month = ""
    previous_amount = 0
    change_amount = 0
    change_amount_total = 0

    #Loop through rows
    for row in csvreader:
        
        #Count total months
        total_months = total_months + 1
        
        #Calculate total amount
        total_amount = total_amount + int(row[1])
        
        #Calculate average change amount
        if previous_amount != 0:
            change_amount = int(row[1]) - previous_amount
            change_amount_total = change_amount_total + change_amount
            average_change = round(change_amount_total / (total_months - 1), 2)
        
        #Calculate greatest increase
        if change_amount > greatest_increase_amount:
            greatest_increase_amount = change_amount
            greatest_increase_month = row[0]

        #Calculate greatest decrease
        if change_amount < greatest_decrease_amount:
            greatest_decrease_amount = change_amount
            greatest_decrease_month = row[0]
        
        #Set previous amount
        previous_amount = int(row[1])

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_amount))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + str(greatest_increase_month) + " ($" + str(greatest_increase_amount) + ")")
print("Greatest Decrease in Profits: " + str(greatest_decrease_month) + " ($" + str(greatest_decrease_amount) + ")")
