# Election Analysis

## Overview of Election Audit

A Colorado Board of Elections employee requested an election audit for a recent local congressional election.  Ballot data including Ballot #, County and Candidate was supplied in a .csv file.

**The deliverables are:**
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
   - Denver:    82.8% (306,055 total votes) **highest voter turnout**
   - Arapahoe:   6.7% (24,801 total votes)
 - Percentage and total number of votes cast by candidate:
   - Charles Casper Stockham:  23.0% (85,213 total votes)
   - Diana DeGette:            73.8% (272,892 total votes)  **winner based on popular vote**
   - Raymon Anthony Doane:      3.1% (11,606 total votes)

### Python Code:  PyPoll_Challenge.py
The completed python script is available **[here}(https://github.com/lnshewmo/Election_Analysis/blob/main/PyPoll_Challenge.py)**
