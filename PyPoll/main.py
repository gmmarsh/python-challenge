#Module for reading CSV files
import os
import csv

#Set path for file
csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")

#Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

#Create variables
    total_votes = 0
    Stockham_votes = 0
    DeGette_votes = 0
    Doane_votes = 0
    Stockham_percent = 0
    DeGette_percent = 0
    Doane_percent = 0
    winner = 0

    #Loop through rows
    for row in csvreader:
        
        #Count total votes
        total_votes = total_votes + 1
        
       #Calculate votes for each candidate
        if row[2] == "Charles Casper Stockham":
            Stockham_votes = Stockham_votes + 1
        elif row[2] == "Diana DeGette":
            DeGette_votes = DeGette_votes + 1
        elif row[2] == "Raymon Anthony Doane":
            Doane_votes = Doane_votes + 1

        # Calculate percentages and format as percentage string
        Stockham_percent = "{:.3f}%".format((Stockham_votes / total_votes) * 100)
        DeGette_percent = "{:.3f}%".format((DeGette_votes / total_votes) * 100)
        Doane_percent = "{:.3f}%".format((Doane_votes / total_votes) * 100)

        #Calculate winner
        if Stockham_votes > DeGette_votes:
            if Stockham_votes > Doane_votes:
                winner = "Charles Casper Stockham"
            else:
                winner = "Raymon Anthony Doane"
        elif DeGette_votes > Doane_votes:
            winner = "Diana DeGette"
        else:
            winner = "Raymon Anthony Doane"

#Print results
print()
print()
print("Election Results")
print()
print("-------------------------")
print()
print("Total Votes: " + str(total_votes))
print()
print("-------------------------")
print()
print("Charles Casper Stockham: " + str(Stockham_percent) + " (" + str(Stockham_votes) + ")")
print()
print("Diana DeGette: " + str(DeGette_percent) + " (" + str(DeGette_votes) + ")")
print()
print("Raymon Anthony Doane: " + str(Doane_percent) + " (" + str(Doane_votes) + ")")
print()
print("-------------------------")
print()
print("Winner: " + str(winner))
print()
print("-------------------------")
print()
print()

#Set path for file
output_path = os.path.join("PyPoll", "Analysis", "PyPoll analysis.txt")

#Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, "w") as txtfile:
    
    #Write results to file
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write("Total Votes: " + str(total_votes) + "\n")
    txtfile.write("-------------------------\n")
    txtfile.write("Charles Casper Stockham: " + str(Stockham_percent) + " (" + str(Stockham_votes) + ")\n")
    txtfile.write("Diana DeGette: " + str(DeGette_percent) + " (" + str(DeGette_votes) + ")\n")
    txtfile.write("Raymon Anthony Doane: " + str(Doane_percent) + " (" + str(Doane_votes) + ")\n")
    txtfile.write("-------------------------\n")
    txtfile.write("Winner: " + str(winner) + "\n")
    txtfile.write("-------------------------\n")