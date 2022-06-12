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







