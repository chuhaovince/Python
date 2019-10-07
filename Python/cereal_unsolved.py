import os
import csv

cereal_csv = os.path.join("cereal_bonus.csv")
with open(cereal_csv,'r',encoding = "utf8") as file:
    # To skip the header, use next()
    # next(csv.reader(file),None)
    readfile = csv.reader(file,delimiter = ',')
    for row in readfile:
        if float(row[7]) >= 5:
            print(row)
