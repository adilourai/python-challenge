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

#Create list of candidates who received votes
candidates_set = set(votes)
candidates = list(candidates_set)

#Calculate total votes for each candidate
votes_total_dict = {}
for name in candidates:
    candidate_total = votes.count(name)
####THIS IS WHERE IT BREAKS!!! GOTTA FIX THE DICTIONARY###
for i in range(len(candidates)):
    votes_total_dict[candidates[i]] = str(candidate_total)[i]

#Calculate percentage of votes won by each candidate
votes_percent_dict = {}
for name in candidates:
    candidate_percent = round((float(votes.count(name) / total_votes)),2)
    for i in range(len(candidates)):
        votes_percent_dict[candidates[i]] = str(candidate_percent)[i]

# print(votes_total_dict["Diana DeGette"])