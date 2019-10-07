import os

filepath = r"F:\\DATA Bootcamp\\UT-TOR-DATA-PT-09-2019-U-C\\Unit 3 - Python\\Classroom Activities\\Class 2\\11-Stu_UdemyZip\\Resources\\web_starter.csv"

import csv

Title = []
Price = []
Subscriber_Cout = []
Num_of_Reviews = []
Course_Length = []

with open(filepath, 'r', encoding="utf8") as file:
    filereader = csv.reader(file, delimiter = ",")
    for row in filereader:
        Title.append(row[1])
        Price.append(row[4])
        Subscriber_Cout.append(row[5])
        Num_of_Reviews.append(row[6])
        Course_Length.append(int(row[9][0]))
    new_data = zip(Title, Price, Subscriber_Cout, Num_of_Reviews, Course_Length)
file.close()

with open("new_Udemy_zip.csv", 'w', newline='', encoding = 'utf8') as writefile:
    filewriter = csv.writer(writefile, delimiter = ",")
    filewriter.writerow(['Title', 'Price', 'Subsriber Count', 'Num of Reviews', 'Course Length'])
    filewriter.writerows(new_data)
writefile.close()