#dependencies
import csv

import os

#assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# open the election results and read the file
with open(file_to_load) as election_data:



    #read and analyze data

    file_reader = csv.reader(election_data)

 #print the header row

    headers = next(file_reader)

    print(headers)