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
    net_total = 0
    profit_change = 0 

# Start loop after header
    header = next(csvreader)
 
    profit_list = []
    months_list = []
# total number of months included in the dataset
# total amount of Profit/Loss over entire period
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

#Calculate the greatest increase in profits and greatest decrease in losses (date and amount) over period
max_profit_increase = max(profit_change)
max_profit_decrease = min(profit_change)

#determine month of max profit increase/decrease
#def find(target, profit_list):
    #for i in range(len(profit_list)):
        #if profit_list[i] == max_profit_increase:
            #yield i 

            #max_profit_increase_month = months_list[i]
            
    #print(months_list[i])

max_profit_increase_index = profit_list.index(max_profit_increase)
max_profit_decrease_index = profit_list.index(max_profit_decrease)
  
print(max_profit_increase_index)
print(max_profit_decrease_index)
   

#print analysis to the terminal 
print("Financial Analysis")
print("--------------------------")
print("Total Months: " + str(month_count))
print("Total: " + "$" + str(net_total))
print("Average change: " + "$" + str(average_profit_change))
#print("Greatest Increase in Profits: " + date + max_profit_increase)
#print("Greatest Decrease in Profits: " + date + max_profit_decrease)


#export text file with results 
