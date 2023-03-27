#Importing files

import os
import csv

# file = os.path.join('Resources', 'election_data.csv')
file = 'C:\\Users\\kanwal\\Documents\\UT Austin Projects\\WEEK 3\\Assignments\\Python_Challenge\\PyPoll\\Resources\\election_data.csv'
# print(file)

# Defining variables
total_votes = 0
candidates = {}
winner = ""
winning_votes = 0

# Read in the CSV file
with open(file, 'r') as csvfile:
    
    # Spliting the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skiping the header row
    next(csvreader)
    
    # Looping through the data
    for row in csvreader:
        
        # Count the total number of votes
        total_votes += 1
        
        # Count the votes for each candidate
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1
            
    # Calculate the percentage of votes for each candidate
    for candidate in candidates:
        votes = candidates[candidate]
        percentage = round(votes/total_votes*100, 3)
        candidates[candidate] = {"votes": votes, "percentage": percentage}
        
        # Determine the winning candidate
        if votes > winning_votes:
            winner = candidate
            winning_votes = votes
            
# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    votes = candidates[candidate]["votes"]
    percentage = candidates[candidate]["percentage"]
    print(f"{candidate}: {percentage}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Write the results to a text file
output_path = os.path.join("PyPoll", "Analysis", "results.txt")
with open("Poll Result.txt", 'w') as outfile:
    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("-------------------------\n")
    for candidate in candidates:
        votes = candidates[candidate]["votes"]
        percentage = candidates[candidate]["percentage"]
        outfile.write(f"{candidate}: {percentage}% ({votes})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner: {winner}\n")
    outfile.write("-------------------------\n")
