#DATA NEEDED
#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote

# Import the datetime class from the datetime module.
# datetime is a DEPENDENCY
import datetime
# Use the now() attribute on the datetime class to get the present time.
# So we are telling it to get the METHOD 'now' out of the 'datetime' CLASS
# from within the 'datetime' MODULE 
# this relationship is called a DEPENDENCY
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)

# To reduce the confusion on importing a module with the same name as a class 
# use an abbreviated alias dt for the datetime module.
# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)
# above comma is to concatenate the string to the DEPENDENCY 'now' 

import csv # csv is a MODULE
dir(csv) # the DIR function shows what is inside the module
# other things (ex. variables, data types) can be put inside dir() and all the 
# available CSV functions # which can be used on the (obj) will be displayed

dir(int)
dir(float)
dir(bool)
dir(list)
dir(tuple)
dir(dict)
dir(datetime)

import random
dir(random)

import numpy

# TO OPEN AND READ A FILE
# create a DIRECT PATH the the PyPoll data file
# METHOD 1
# assign a variable for the file to load and the path
import csv
file_to_load = 'Resources/election_results.csv'
# open the election results and read the file
# election_data is the file variable
election_data = open(file_to_load,'r')

# to do: perform the analysis

# close the file which also saves the data
election_data.close()

# METHOD 2
import csv
# assign a variable for the file to load and the path
file_to_load = 'Resources/election_results.csv'
# open the election results and read the file
with open(file_to_load) as election_data:

# to do: perform the analysis

    print(election_data)

# INDIRECT PATH to the file
import csv
import os
# Assign a variable = 
# then CHAIN the os.path submodule with join() to join the folder and file join(folder,file)
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results csv and read the file.
with open(file_to_load) as election_data:  # naming variable 

    # Print the file object.
     print(election_data)


# TO WRITE DATA TO A FILE
# create a filename variable to a direct or indirect path to the ifle
import csv
import os
file_to_save = os.path.join("analysis","election_analysis.txt")
# use the open() function with "w" mode will write data to the file
open(file_to_save,'w')

# send data to the file analysis.txt
# create a filename variable to a direct or indirect path to the file
# the file we are saving is "election_analysis.txt" located in folder "analysis"
import csv
import os
file_to_save = os.path.join("analysis","election_analysis.txt")
# use the open statement to open the file as a text file
outfile = open(file_to_save,"w")
# write some data to the file
outfile.write("Hello World") # the function write() is in the OS MODULE
# close the file
outfile.close

# refactor the code using WITH instead of open() and close()
import csv
import os
# create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis","election_analysis.txt")
# using the WITH statement to open the file as a .txt
with open(file_to_save,"w") as txt_file:
    # write some data to the file
    txt_file.write("Arapahoe, Denver, Jefferson")
