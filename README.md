![](https://github.com/lnshewmo/Election_Analysis/blob/main/voting%20banner.jpg)
# Election Analysis

## Overview of Election Audit

A Colorado Board of Elections employee requested an election audit for a recent local congressional election.  Ballot data including Ballot #, County and Candidate was supplied in a .csv file.

**The required deliverables are given as:**
 1. Total number of votes cast
 2. Total number and percentage of votes cast by county
 3. The county with the highest voter turnout
 4. Total number and percentage of votes cast for each Candidate
 5. The winner of the election based on popular vote

## Resources
- Data Source: **[election_results.csv](https://github.com/lnshewmo/Election_Analysis/blob/main/resources/election_results.csv)**
- Software: Python 3.9.12, Visual Studio Code 1.68

## Election Audit Results

### Election Outcomes
- Total number of votes cast: 369,711
- Percentage and total number of votes cast by county:
   - Jefferson: 10.5% (38,855 total votes)
   - Denver:    82.8% (306,055 total votes)  **\**highest voter turnout\****
   - Arapahoe:   6.7% (24,801 total votes)
 - Percentage and total number of votes cast by candidate:
   - Charles Casper Stockham:  23.0% (85,213 total votes)
   - Diana DeGette:            73.8% (272,892 total votes)  **\**winner based on popular vote\****
   - Raymon Anthony Doane:      3.1% (11,606 total votes)

### Python Code:  PyPoll_Challenge.py
- The completed python script is available **[here](https://github.com/lnshewmo/Election_Analysis/blob/main/PyPoll_Challenge.py)**
- Results were also printed to **[election_analysis.txt](https://github.com/lnshewmo/Election_Analysis/blob/main/analysis/election_analysis.txt)**
- Running PyPoll_Challenge.py script in VS Code gives the following terminal output: ![image PyPoll terminal](/analysis/terminal.png)

## Election Audit Summary

The winner of this election, according to popular vote, is Diana DeGette with 73.8% over the vote (272,892 total votes).
The county with largest election turnout (82.8% of the total ballots and 306,055 of the total votes) is Denver county.

### Future Use

This script is dynamic enough exactly as it is to support re-use for any election audit of the same type - a unique ballot id, multiple county names and mutiple candidate names - when the required deliverables are the same.  The name and path of the .csv `file_to_load` should be updated, and a new name and path to the `file_to_save` should also be specified.  The output will be in the same format.   The supplied .csv file can contain any number of county names and candidates.  

More broadly, it can also support an analysis where instead of candidate names, any set of ballot initiatives or measures are listed in that column instead.  

Similarly to County Votes, another demographic variable associated with the ballot could be explored and added to the code in another set of `for` loops.  For example, if the party affiliation of the voter is available, the script could be expanded by initializing a counter for `party_vote`.  Subsequent code blocks for this new varible would be added under each section just as the county blocks are setup.  Another `if` statement in the `for row in reader:` loop will extract and manipulate the party data.  To print the additional output, an added `for` loop in front of the section `for county_name in county_votes:` would render the party percentages and turnout.

