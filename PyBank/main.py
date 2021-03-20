#import modules
import os
import csv

#create path
csvpath = os.path.join("Resources", "budget_data.csv")

#open file and specify container and delimiter
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter= ',')

#Initiate counter and define starting value 
    month_count = 0
    net_total = 0
    profit_change = 0 

#Start loop after header
    header = next(csvreader)
 
#Create lists 
    profit_list = []
    months_list = []

#Calculate total number of months included in the dataset
#total amount of Profit/Loss over entire period
    for row in csvreader: 
        net_total += int(row[1])
        profit_list.append(int(row[1]))
        months_list.append(row[0])
        month_count += 1

#calculate changes in "Profit/Losses" over the entire period 
    profit_change = []
    a = 0 
    b = 1 
while b < len(profit_list):
    change = profit_list[b] - profit_list[a]
    profit_change.append(change)
    a = b 
    b = b + 1 

total_profit_change = sum(profit_change)

#find the average of the above changes
average_profit_change = round(total_profit_change / len(profit_change), 2)

#Calculate the greatest increase in profits and greatest decrease in losses over period
max_profit_increase = max(profit_change)
max_profit_decrease = min(profit_change)

#determine index of greatest increase/decrease
max_profit_increase_index = profit_change.index(max_profit_increase)
max_profit_decrease_index = profit_change.index(max_profit_decrease)

#determine month of max profit increase and max profit decrease
max_increase_month = months_list[(max_profit_increase_index)+1]
max_decrease_month = months_list[(max_profit_decrease_index)+1]   

#print analysis to the terminal 
print("Financial Analysis")
print("--------------------------")
print("Total Months: " + str(month_count))
print("Total: " + "$" + str(net_total))
print("Average change: " + "$" + str(average_profit_change))
print("Greatest Increase in Profits: " + str(max_increase_month) + " ($" + str(max_profit_increase) + ")")
print("Greatest Decrease in Profits: " + str(max_decrease_month) + " ($" + str(max_profit_decrease) + ")")

#export analysis to text file
output_file = os.path.join("Analysis", "PyBankAnalysis.txt")
with open(output_file, "w") as f:
    print("Financial Analysis", file = f)
    print("--------------------------", file = f)
    print("Total Months: " + str(month_count), file = f)
    print("Total: " + "$" + str(net_total), file = f)
    print("Average change: " + "$" + str(average_profit_change), file = f)
    print("Greatest Increase in Profits: " + str(max_increase_month) + " ($" + str(max_profit_increase) + ")", file = f)
    print("Greatest Decrease in Profits: " + str(max_decrease_month) + " ($" + str(max_profit_decrease) + ")", file = f)
f.close()

