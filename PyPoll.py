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

# Open the election results and read the file
with open(file_to_load) as election_data:

# Read the file object with the reader function
    file_reader = csv.reader(election_data)

# print the header (verify the first row is the header)
    headers = next(file_reader)
    print(headers)

# Print each row in the CSV file
   for row in file_reader:
        print(row) # prints the whole file
       # print(row[0]) # Prints just the first column of each row