import os
import csv

# Path to collect data from the Resources folder

# Define the function and have it accept the 'wrestlerData' as its sole parameter
wrestling_csv = os.path.join('WWE-Data-2016.csv')
def print_percentages(wrestler_data):
    global wins, losses, draws
    total = int(wrestler_data[1]) + int(wrestler_data[2]) + int(wrestler_data[3])
    wins = int(wrestler_data[1])/total
    losses = int(wrestler_data[2])/total
    draws = int(wrestler_data[3])/total
    return 
# Find the total number of matches wrestled

# Find the percentage of matches won

# Find the percentage of matches lost

# Find the percentage of matches drawn

# Print out the wrestler's name and their percentage stats

# Read in the CSV file
with open(wrestling_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if(name_to_check == row[0]):
            print_percentages(row)
            print(wins, losses, draws)
