
#Import the os module
import os
#Module for reading CSV file
import csv

csvpath = os.path.join('PyBank','Resources','budget_data.csv')

#Reading CSV file
with open(csvpath) as csvfile:
    #CSV reader will specify delimiter and the variable that holds the contents
    csvreader = csv.reader(csvfile,delimiter=',')
    print(csvreader)

    #Read header row
    csv_header = next(csvreader)

    #Setting counters for month,total Profit/Losses, Profit/Losses value and change
    Months = 0
    TotalPL = 0
    PLValue = 0
    Change = 0
    #Setting lists for Profit and Date
    Profit = []
    Date = []

    #Reading the first row 
    first_row = next(csvreader)
    Months +=1
    TotalPL += int(first_row[1])
    PLValue = int(first_row[1])
  
    #Read each row after the header
    for row in csvreader:
        
        #Keeping a list of all dates 
        Date.append(row[0])

        #Change is calculated and than stored in profit list
        Change = int(row[1]) - PLValue
        Profit.append(Change)
        PLValue = int(row[1])

        #Add to month count
        Months += 1

        #Calculate total PL over the entire period
        TotalPL = TotalPL + int(row[1])

    #Find greatest increase amount and date
    Increase = max(Profit)
    IncreaseIndex = Profit.index(Increase)
    IncreaseDate = Date[IncreaseIndex]

    #Find greatest decrease amount and date
    Decrease = min(Profit)
    DecreaseIndex = Profit.index(Decrease)
    DecreaseDate = Date[DecreaseIndex]

    #Calculate average change in PL
    Average = sum(Profit) / len(Profit)

    #Print results
    print("Financial Analysis")
    print("---------------------")
    print(f"Total Months: {Months}")
    print(f"Total: ${TotalPL}")
    print(f"Average Change: ${round(Average,2)}")
    print(f"Greatest Increase in Profits: {IncreaseDate} (${Increase})")
    print(f"Greatest Decrease in Profits: {DecreaseDate} (${Decrease})")

    #Specify file to write to
    output = os.path.join("PyBank","output.txt")

    #List of text for each line
    lines = ["Financial Analysis","---------------------",f"Total Months: {Months}",
             f"Total: ${TotalPL}",f"Average Change: ${round(Average,2)}",f"Greatest Increase in Profits: {IncreaseDate} (${Increase})",
             f"Greatest Decrease in Profits: {DecreaseDate} (${Decrease})"]
    #Open file using write mode
    #Reference: Write text file > https://www.pythontutorial.net/python-basics/python-write-text-file/
    with open(output,"w") as f:
        f.write('\n'.join(lines))