
#not solid on what this means but it's in a bunch of activities

import os
import csv

BudgetCSV = os.path.join('budget_data.csv')

#make some blank lists to hold stuff
TotalMonths = []
TotalProfit = []
ProfitChange = []

#used these prints to see what's going on
#print(TotalMonths)
#print(TotalProfit)
#print(ProfitChange)



# Read in the CSV file
#with open(wrestlingCSV, 'r') as csvfile:
#
#   # Split the data on commas
#    csvreader = csv.reader(csvfile, delimiter=',')
#
#    header = next(csvreader)

#reads my budget_data.csv, seperates with a , and then skips the header
with open(BudgetCSV, 'r') as BudgetData:
    BudgetData = csv.reader(BudgetData, delimiter=',')
    header = next(BudgetData)

#this is where things got complicated and I relied heavily on the internet and then Justin and Courtney helped me a lot in understanding what's happening
#so we've read in my csv file called it BudgetData and seperated it at a ,
#Now we're assigning everything in index 0 of BudgetData to the list TotalMonths, essentially a count of all the months or a count of all the rows
#same thing for TotalProfit, we're calling everything in index 1 of BudgetData an int and dumping it into the list TotalProfit
#as verified below in print(TotalMonths) and print(TotalProfits), now we have 2 lists assigned to the 2 variable TotalMonths and TotalProfits
    for DataRow in BudgetData: 
        TotalMonths.append(DataRow[0])
        TotalProfit.append(int(DataRow[1]))

#ok so for every index in range(evaluation of all the indexes in TotalProfit -1), 85 in this case and -1 cause we start at 0 and
#we want to capture our last row by subtracting our current position in the loop, from the last position. 
#ie, there are actually 86 months, we are subtracting our current position in the loop, from the one following i+1. If we don't -1,
#then we subtract TotalProfit from itself and it returns 0
  #  for i in range(len(TotalProfit)):
  #      ProfitChange.append(TotalProfit[i]-TotalProfit[i])
#or we subtract our current position in the loop from the following position, and when we hit 86, the final loop
#we end up subtracting from information that isn't there and receive this error
#Traceback (most recent call last):
#     for i in range(len(TotalProfit)):
#        ProfitChange.append(TotalProfit[i+1]-TotalProfit[i])     
    for i in range(len(TotalProfit)-1):
        ProfitChange.append(TotalProfit[i+1]-TotalProfit[i])

#snags the highest number in the list ProfitChange and assigns it to variable MaxIncrease         
MaxIncrease = max(ProfitChange)
#snags the the lowest number in list ProfitChange and assigns it to variable MaxDecrease
MaxDecrease= min(ProfitChange)

#ProfitChange has 85 entries instead of 86 like TotalProfit and TotalMonths. During:
#for i in range(len(TotalProfit)-1):
#        ProfitChange.append(TotalProfit[i+1]-TotalProfit[i])
#each iteration added 1 more item/index to the end of the list ProfitChange, since the first month had no previous month to subtract from, the list is off by 1
#adding 1 to the index location of ProfitChange.index(max(ProfitChange)) aligns the highest value in ProfitChange with it's corresponding month
MaxIncrease_Month = ProfitChange.index(max(ProfitChange)) + 1
MaxDecrease_Month = ProfitChange.index(min(ProfitChange)) + 1 

#these prints are what I used to see what's going on in the code
#print(BudgetData)
#print(TotalMonths)
#print(TotalProfit)
#print(len(ProfitChange)) 
#print(len(TotalProfit)-1)
#print(MaxIncrease)
#print(MaxDecrease)
#print(MaxIncrease_Month)
#print(MaxDecrease_Month)
#print(len(ProfitChange))
#print("_______________________________________________________")
#Print all that junk out
print("Financial Analysis")
print("_______________________________________________________")
#print the number of indexes in TotalMonths
print(f"Total Months: {len(TotalMonths)}")
#print the sum of the indexes in TotalProfit
print(f"Total: ${sum(TotalProfit)}")
#print the average change by dividing the sum of ProfitChange by the number of idexes/intances in ProfitChange, rounding the number to 2 decimal places
print(f"Average Change: {round(sum(ProfitChange)/len(ProfitChange),2)}")
#Print the contents of TotalMonths index as indicated by (the value of)MaxIncrease_Month and also print the value of MaxIncrease
print(f"Greatest Increase in Profits: {TotalMonths[MaxIncrease_Month]} (${MaxIncrease})")
#Print the contents of TotalMonths index as indicated by (the value of)MaxDecrease_Month and also print the value of MaxDecrease
print(f"Greatest Decrease in Profits: {TotalMonths[MaxDecrease_Month]} (${(MaxDecrease)})")

#make a file in the current directory called BudgetAnalysis.txt and assign it to the variable BudgetAnalysisOutput
BudgetAnalysisOutput = os.path.join(".", "BudgetAnalysis.txt")

#open BudgetAnalysis.txt for writing
with open(BudgetAnalysisOutput,"w") as Output:

#add the output of the Financial Analysis into the text file
    Output.write("Financial Analysis \n")
    Output.write("_______________________________________________________ \n")
    Output.write(f"Total Months: {len(TotalMonths)} \n")
    Output.write(f"Total: ${sum(TotalProfit)} \n")
    Output.write(f"Average Change: {round(sum(ProfitChange)/len(ProfitChange),2)} \n")
    Output.write(f"Greatest Increase in Profits: {TotalMonths[MaxIncrease_Month]} (${(MaxIncrease)}) \n")
    Output.write(f"Greatest Decrease in Profits: {TotalMonths[MaxDecrease_Month]} (${(MaxDecrease)}) \n")
