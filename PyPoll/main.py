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

        #Calculate percentages
        Stockham_percent = round((Stockham_votes / total_votes) * 100, 2)
        DeGette_percent = round((DeGette_votes / total_votes) * 100, 2)
        Doane_percent = round((Doane_votes / total_votes) * 100, 2)

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

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
print("Charles Casper Stockham: " + str(Stockham_votes) + " " + str(Stockham_percent))
print("Diana DeGette: " + str(DeGette_votes) + " " + str(DeGette_percent))
print("Raymon Anthony Doane: " + str(Doane_votes) + " " + str(Doane_percent))
print("-------------------------")
print("Winner: " + str(winner))
