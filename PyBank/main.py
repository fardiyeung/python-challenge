# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

# Method 2: Improved Reading using CSV module


totalMonths = 0
totalNet = 0
averageChange = 0
greatestIncrease = 0
greatestDecrease = 0



with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #totalMonths = len(csvreader)
    #totalNet = [int(item[1]) += int(item[1]) for item in cvsreader]
    #averageChange = totalNet / totalMonths

    # 
    currentIncreaseDate = ''
    currentDecreaseDate = ''

    # Read each row of data after the header
    for row in csvreader:
        currentProfitLoss = int(row[1])
        currentDate = row[0]
        totalNet += int(row[1])
        # get a total number of month
        totalMonths += 1
        #get the greatest Increase 
        if (currentProfitLoss > greatestIncrease) & (currentProfitLoss > 0):
            greatestIncrease = currentProfitLoss
            currentIncreaseDate = currentDate
        #get the greatest decrease
        if (currentProfitLoss < greatestDecrease) & (currentProfitLoss < 0):
            greatestDecrease = currentProfitLoss
            currentDecreaseDate = currentDate

    averageChange = totalNet / totalMonths

    def add_line(line):
        return line + "\n"

    output1 = "Financial Analysis"
    output2 = "----------------------------"
    output3 = f"Total Months: {totalMonths}"
    output4 = f"Total: ${totalNet}"
    output5 = f"Average  Change: ${averageChange}"
    output6 = f"Greatest Increase in Profits: {currentIncreaseDate} (${greatestIncrease})"
    output7 = f"Greatest Decrease in Profits: {currentDecreaseDate} (${greatestDecrease})"

    print(output1)
    print(output2)
    print(output3)
    print(output4)
    print(output5)
    print(output6)
    print(output7)

   
    # write lines to file

    with open("pyBank.txt",'w',encoding = 'utf-8') as f:
        f.write(add_line(output1))
        f.write(add_line(output2))
        f.write(add_line(output3))
        f.write(add_line(output4))
        f.write(add_line(output5))
        f.write(add_line(output6))
        f.write(output7)

    

