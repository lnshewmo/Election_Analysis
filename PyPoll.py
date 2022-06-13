#DATA NEEDED
#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote

# Add dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initialize an ACCUMULATOR variable (like an index)
# initialize a total vote counter
# placement is before opening the file to read
total_votes = 0

# declare a new list for candidate data
candidate_options = []
# declare a dictionary to hold the {names:votes}
candidate_votes = {}
# declare variables for winning_candidate, winning_count, and winning_percentage
# set winning_count and winning_percentage to zero
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

# Read the file object with the reader function
    file_reader = csv.reader(election_data)

# print the header (verify the first row is the header)
    headers = next(file_reader)
    # print(headers) # activate this to see them

# Print each row in the CSV file
    for row in file_reader:
            # print(row) # prints the whole file
            # print(row[0]) # Prints just the first column of each row

            # add to the total_vote count
            total_votes += 1
            
            # get the candidate name from each row[2]
            candidate_name = row[2]

            # if the candidate name does not match any current name
            if candidate_name not in candidate_options:

                # append candidate name to the candidate options list
                candidate_options.append(candidate_name) # print(candidate_options) here gives a list of 3 names

                # make the candidate names the key for {candidate vote} and set count to 0
                candidate_votes[candidate_name] = 0

            # add votes to each name
            candidate_votes[candidate_name] += 1
            # this loop is complete and the names and total votes for each name have been collected

# determine the percentage of total votes for each candidate by looping through the counts
# iterate through the candidate list
for candidate_name in candidate_votes:
    # get the vote count of a candidate
    votes = candidate_votes[candidate_name] # defines votes as the KEY in {candidate_votes}
    #calculate the percentage of votes and convert values from int to float
    vote_percentage = float(votes)/float(total_votes) *100

    # to do: print out each candidate's name, vote count, percentage votes
    # votes to the terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # determine winning count vote and candidate
    # determing if VOTES is greater than the winning count
    if (votes>winning_count) and (vote_percentage>winning_percentage):

        # if true, set winning_count = votes and winning_percentage = vote_percentage
        winning_counts = votes
        winning_percentage = vote_percentage
        # set the winning_candidate = candidate_name
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)




    # print candidate name with percentage of votes
    print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote")


#print the candidate list
print(candidate_options)

# print the total_votes
print(total_votes)

print(candidate_votes)
