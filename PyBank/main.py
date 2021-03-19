#import modules
import os
import csv

#create path
csvpath = os.path.join("Resources", "budget_data.csv")

#open file and specify container and delimiter
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter= ',')

# Initiate counter and define starting value 
    month_count = 0
    total_profit = 0
    total_loss = 0
    net_total = 0
    profit = 0
    profit_change = 0 

# Start loop after header
    header = next(csvreader)

# total number of months included in the dataset
# total amount of Profit/Loss over entire period
    for row in csvreader:
        month_count += 1 
        net_total += int(row[1])
    #for row in csvreader:
        #profit = int(row[1])
    #if profit > 0:
       # total_profit = total_profit + int(row[1])
    #elif profit < 0:
        #total_loss = total_loss + int(row[1])

        #net_total = total_profit - total_loss 

    for x in range(row):
        profit_change = int(x[1])-int((x-1)[1])
        #profit_change += profit_change 
       
# i from i+1  = change in profit 
#continue through loop and add each to change in profit 

#calculate changes in "Profit/Losses" over the entire period 

    #find the average of the above changes

#Calculate the greatest increase in profits (date and amount) over period
#create a dictionary grt_profit = {row[0]:int(row[1])}

#Calculate the greatest decrease in losses (date and amount) over period

#print analysis to the terminal 
print("Financial Analysis")
print("--------------------------")
print("Total Months: " + str(month_count))
print("Total: " + "$" + str(net_total))
print(profit_change)
#print("Average change: " + "$" + average_change)
#print("Greatest Increase in Profits: " + date + grt_profit)
#print("Greatest Decrease in Profits: " + date + grt_loss)


#export text file with results 
