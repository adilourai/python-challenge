#Import csv module
import csv

#Create list to store values for analysis
votes = []

#Read csv file, store headings separately, and populate votes list with data
with open("C:/Users/adina/Desktop/Classwork/Module 3 Python/Module 3 Challenge/python-challenge/PyPoll/Resources/election_data.csv") as csvfile:
    csvreader = csv.reader(csvfile)
    headings = next(csvreader)
    for row in csvreader:
        votes.append(row[2])

#Calculate total number of votes
total_votes = float(len(votes))
    
#Create list of candidates who received votes; alphabetize list to keep results consistent
candidates = list(set(votes))
candidates.sort()

#Calculate total votes for each candidate using a vote counting function and storing values in a dictionary
votes_total_dict = {}

def candidate_votes(name):
    vote_count = 0
    for vote in votes:
        if vote == name:
            vote_count += 1
    votes_total_dict[name] = vote_count

for name in candidates:
    candidate_votes(name)

#Calculate percentage of votes won by each candidate using a function to calculate and then format as percent, and store in dictionary
votes_percent_dict = {}

def candidate_percentages(name):
    percent = str(round(((votes_total_dict[name] / total_votes) * 100),3)) + "%"
    votes_percent_dict[name] = percent

for name in candidates:
    candidate_percentages(name)

#Determine winner
most_votes = max(votes_total_dict.values())
winner = {name for name in votes_total_dict if votes_total_dict[name]==most_votes}

#Print results to terminal
print("Election Results\n")
print("--------------------\n")
print("Total Votes: " + str(int(total_votes)) + "\n")
print("--------------------\n")
for name in candidates:
    print(f'{name}: {votes_percent_dict[name]} ({votes_total_dict[name]})\n')
print("--------------------\n")
print("Winner: ",end="")
print(*winner)
print("\n--------------------")

#Create output .txt file and write results into file
output_file = open("C:/Users/adina/Desktop/Classwork/Module 3 Python/Module 3 Challenge/python-challenge/PyPoll/Analysis/PyPoll_Analysis.txt", "w")

output_file.write
output_file.write("Election Results\n")
output_file.write("--------------------\n")
output_file.write("Total Votes: " + str(int(total_votes)) + "\n")
output_file.write("--------------------\n")
for name in candidates:
    output_file.write(f'{name}: {votes_percent_dict[name]} ({votes_total_dict[name]})\n')
output_file.write("--------------------\n")
output_file.write("Winner: ")
output_file.write(*winner)
output_file.write("\n--------------------")

output_file.close()