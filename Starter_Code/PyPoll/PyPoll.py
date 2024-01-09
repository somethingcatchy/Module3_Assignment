import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader, None)

    Total_votes = 0
    data_rows = []
    Votes_Charles = 0
    Votes_Diana = 0
    Votes_Raymon = 0

    for rows in csvreader:
        Total_votes += 1
        data_rows.append(rows)

        
        if rows[2] == "Charles Casper Stockham":
            Votes_Charles += 1
            

        if rows[2] == "Diana DeGette":
            Votes_Diana += 1

        if rows[2] == "Raymon Anthony Doane":
            Votes_Raymon += 1

Percentage_Charles = ((Votes_Charles)/Total_votes)*100
Percentage_Diana = ((Votes_Diana)/Total_votes)*100
Percentage_Raymon = ((Votes_Raymon)/Total_votes)*100

Round_Charles = round(Percentage_Charles, 3)
Round_Diana = round(Percentage_Diana, 3)
Round_Raymon = round(Percentage_Raymon, 3)

print("Election Results", end = '\n\n')

print("-"*100, end = '\n\n')

print(Total_votes, end = '\n\n')

print("-"*100, end = '\n\n')

print(f"Charles Casper Stockham: {Round_Charles}% ({Votes_Charles})", end = '\n\n')
print(f'Diana DeGette: {Round_Diana}% ({Votes_Diana})', end = '\n\n')
print(f"Raymon Anthony Doanne: {Round_Raymon}% ({Votes_Raymon})", end = '\n\n')

print("-"*100, end = '\n\n')

winner = max((Votes_Charles, "Charles Casper Stockham"), (Votes_Diana, "Diana DeGette"), (Votes_Raymon, "Raymon Anthony Doanne"))

print(f"Winner: {winner[1]}", end = '\n\n')

print("-" * 100)

