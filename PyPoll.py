# Import dependencies
import csv
import os

# Add a variable to load a file from a path. 
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Gather total votes
total_votes = 0

# Gather candidate information
candidate_options = []
candidate_votes = {}

# Gather the county information
county_names = []
county_votes = {}

# For calculating and declaring the winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# For calculating and declaring the county with the bast turnout
largest_county_turnout = ""
largest_county_vote = 0

# With statement to work through the data
with open (file_to_load) as election_data:
    reader=csv.reader (election_data) 

    header = next(reader)


    # For loop to loop
    for row in reader: 

        # count the votes
        total_votes +=1

        # this is where to find the candidate names
        candidate_name = row[2]
        
        # this is where to find the county names
        county_name = row[1]

        # If statement 
        if candidate_name not in candidate_options:
            # add the candidate name to the candidate options list 
            candidate_options.append(candidate_name)

            # collect the candidate options list as the candidate name keys in the dict, candidate votes
            candidate_votes[candidate_name] = 0

        # add one to the candidate name value for each row where it is listed
        candidate_votes[candidate_name] +=1

        # do the same stuff with the counties
        if county_name not in county_names:
            county_names.append(county_name)
            county_votes[county_name] =0
        county_votes[county_name] +=1

# after gathering the data, do some calculations and write a text file
with open(file_to_save, "w") as textfile:

    # total votes is already complete so go ahead and write it 
    election_results = (f'''    
    Election Results
    -------------------------
    Total Votes: {total_votes:,}
    -------------------------
    County Votes:
    ''')
    print(election_results)
    textfile.write(election_results)

    
    for county in county_votes:
        county_vote = county_votes[county]
        county_percent = county_vote / total_votes * 100
        county_results = (
            f"{county}:{county_percent:.1f}% ({county_vote:,})\n    ")
        print (county_results)
        textfile.write(county_results) 

        if (county_vote > largest_county_vote):
            largest_county_vote = county_vote
            largest_county_turnout = county

    largest_county_turnout=(
        f'''
    -------------------------
    Largest County Turnout: {largest_county_turnout}
    -------------------------
    ''')
    print(largest_county_turnout)
    textfile.write(largest_county_turnout)

    for candidate_name in candidate_votes:
        votes = candidate_votes.get(candidate_name)
        vote_percent = votes / total_votes * 100
        candidate_results = (f"{candidate_name}: {vote_percent:.1f}% ({votes:,})\n    ")
        print(candidate_results)
        textfile.write(candidate_results)

        if (votes > winning_count) and (vote_percent > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percent

    winning_candidate_summary = (f'''
    -------------------------
    Winner: {winning_candidate}
    Winning Vote Count: {winning_count:,}
    Winning Percentage: {winning_percentage:.1f}%
    -------------------------

    ''')
    print(winning_candidate_summary)
    textfile.write (winning_candidate_summary)