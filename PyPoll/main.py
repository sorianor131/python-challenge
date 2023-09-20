
#Import the os module
import os
#Module for reading CSV file
import csv

csvpath = os.path.join('PyPoll','Resources','election_data.csv')

#Reading CSV file
with open(csvpath) as csvfile:
    #CSV reader will specify delimiter and the variable that holds the contents
    csvreader = csv.reader(csvfile,delimiter=',')
    print(csvreader)

    #Read header row
    csv_header = next(csvreader)

    #Setting lists for candidates, number of votes and percentage of votes
    Candidates = []
    NumberVotes = []
    PercentageVotes = []
    #Setting counter for total number of votes
    TotalVotes = 0

    for row in csvreader:
        TotalVotes += 1
         #Check if the candidate is part of our list, if not than add his/her name along with a vote
        if row[2] not in Candidates:
            Candidates.append(row[2])
            CandidateIndex = Candidates.index(row[2])
            NumberVotes.append(1)
        #If candidate exists than just add a vote to his/her name
        else:
            CandidateIndex = Candidates.index(row[2])
            NumberVotes[CandidateIndex] += 1

    #Calculate percentage and add it to the percentage votes list
    for votes in NumberVotes:
        Percentage = (votes/TotalVotes)
        #Reference: Format percentage > https://blog.finxter.com/how-to-print-a-percentage-value-in-python/
        Percentage = "{:.3%}".format(Percentage)
        PercentageVotes.append(Percentage)

    #Find the winner
    Winner = max(NumberVotes)
    WinnerIndex = NumberVotes.index(Winner)
    WinningCandidate = Candidates[WinnerIndex]

#Print results
print("Election Results")
print("---------------------")
print(f"Total Votes: {TotalVotes}")
print("----------------------")

for i in range(len(Candidates)):
    print(f"{Candidates[i]}: {PercentageVotes[i]} ({NumberVotes[i]})")
print("-----------------------")
print(f"Winner: {WinningCandidate}")
print("------------------------")

#Specify file to write to
output = os.path.join("PyPoll","output.txt")

#Open file using write mode
#Reference: Write text file > https://www.pythontutorial.net/python-basics/python-write-text-file/
with open(output,"w") as file:
    l1 = "Election Results\n"
    l2 = "---------------------\n"
    l3 = f"Total Votes: {TotalVotes}\n"
    l4 = "----------------------\n"
    file.writelines([l1,l2,l3,l4])

    for i in range(len(Candidates)):
        file.write(f"{Candidates[i]}: {PercentageVotes[i]} ({NumberVotes[i]})\n")

    l5 = "-----------------------\n"
    l6 = f"Winner: {WinningCandidate}\n"
    l7 = "------------------------\n"
    file.writelines([l5,l6,l7])
