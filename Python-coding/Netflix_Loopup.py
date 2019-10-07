import pandas as pd

netflix_data = pd.read_csv('netflix_ratings.csv')

tit = input("What video are you looking for？\n")

if netflix_data['title'].str.contains(tit).any():
    for lab, row in netflix_data.iterrows():
        # print(row)
        if tit == row['title']:
            print(tit + " is rated " + row['rating'] + " with a rating of " + str(row['user rating size']))
            break
else:
    print("Sorry, the video could not be found!")
