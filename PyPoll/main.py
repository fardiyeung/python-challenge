# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')

# Method 2: Improved Reading using CSV module



with open(csvpath) as csvfile:
    mpg = list(csv.DictReader(csvfile))
    Candidate = set(d['Candidate'] for d in mpg)
    print(Candidate)
