#import modules
import os
import csv

#create path
csvpath = os.path.join("Resources", "election_data.csv")

#open file and specify container and delimiter
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter= ',')

#Initiate counter and define starting values
    total_votes = 0 
    khan_votes = 0 
    correy_votes = 0 
    li_votes = 0 
    otooley_votes = 0 

#Start loop after header
    header = next(csvreader)

#Create candidate list
    candidate_list = []

#Calculate total number of votes cast
    for row in csvreader:
        total_votes += 1

#Provide complete list of candidates 
        candidate_list.append(row[2])  

#Calculate total number of votes each candidate won
        if(row[2]== "Khan"):
            khan_votes = khan_votes + 1
        elif(row[2]== "Correy"):
            correy_votes = correy_votes + 1
        elif(row[2]== "Li"):
            li_votes = li_votes + 1
        elif(row[2]== "O'Tooley"): 
            otooley_votes = otooley_votes + 1

#Provide unique list of candidates (positioned here to be outside of loop)
unique_list = list(dict.fromkeys(candidate_list))        

#Calculate percentage of votes each candidate won
khan_percent = round((khan_votes / total_votes) * 100, 4)
correy_percent = round((correy_votes / total_votes)* 100, 4)
li_percent = round((li_votes / total_votes) * 100, 4)
otooley_percent = round((otooley_votes / total_votes) * 100, 4)

#Calculate winner of the election based on popular vote 
total_votes_list = [int(khan_votes), int(correy_votes), int(li_votes), int(otooley_votes)]
winner = max(total_votes_list)

if winner == khan_votes:
    winner = "Khan"
elif winner == correy_votes:
    winner = "Correy"
elif winner == li_votes:
    winner = "Li"
elif winner == otooley_votes:
    winner = "O'Tooley"

#print analysis in terminal
print("Election Results")
print("--------------------------")
print("Total Votes: " + str(total_votes))
print("--------------------------")
print("Khan: " + str(khan_percent) + "% " + "(" + str(khan_votes) + ")")
print("Correy: " + str(correy_percent) + "% " + "(" + str(correy_votes) + ")")
print("Li: " + str(li_percent) + "% " + "(" + str(li_votes) + ")")
print("O'Tooley: " + str(otooley_percent) + "% " + "(" + str(otooley_votes) + ")")
print("--------------------------")
print("Winner: " + winner)
print("--------------------------")

#export text file with results 
output_file = os.path.join("Analysis", "PyPollAnalysis.txt")
with open(output_file, "w") as f:
    print("Election Results", file = f)
    print("--------------------------", file = f)
    print("Total Votes: " + str(total_votes), file = f)
    print("--------------------------", file = f)
    print("Khan: " + str(khan_percent) + "% " + "(" + str(khan_votes) + ")", file = f)
    print("Correy: " + str(correy_percent) + "% " + "(" + str(correy_votes) + ")", file = f)
    print("Li: " + str(li_percent) + "% " + "(" + str(li_votes) + ")", file = f)
    print("O'Tooley: " + str(otooley_percent) + "% " + "(" + str(otooley_votes) + ")", file = f)
    print("--------------------------", file = f)
    print("Winner: " + winner, file = f)
    print("--------------------------", file = f)
f.close()