# Add our dependencies.
import csv
import os
from tkinter.tix import COLUMN
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
county_total_votes = 0

# Candidate Options and votes
candidate_options = []
candidate_votes = {}

#county options and votes
county_options = []
county_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#winning county and tracker
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

# Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]
        county_name = row[1]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            #begin tracking votes
            candidate_votes[candidate_name] = 0

            #add a vote to candidates count
        candidate_votes[candidate_name] += 1
 # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:

 
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0
        county_votes[county_name] += 1
    


# save the results to our text file.
with open(file_to_save, "w") as txt_file:

# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"County Votes:\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

#county votes
    for county_name in county_votes:
        cvotes = county_votes[county_name]
        cvote_percentage = float(cvotes) / float(total_votes) * 100

        county_results = (f"{county_name}: {cvote_percentage:.1f}% ({cvotes:,})\n")
        print (county_results)

        txt_file.write(county_results)

        if (cvotes > winning_county_count) and (cvote_percentage > winning_county_percentage):
        
            winning_county_count = cvotes
            winning_county_percentage = cvote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            cwinning_candidate = county_name
    cwinning_candidate_summary = (
        f"-------------------------\n"
        f"Largest County turnout: {cwinning_candidate}\n"
        f"-------------------------\n")

    print(cwinning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(cwinning_candidate_summary)

        

        # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        #  To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
#  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)