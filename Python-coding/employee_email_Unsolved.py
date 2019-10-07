# @TODO: Your code here
import csv
emails = []
new_employee_data = []
with open('employees.csv', newline = '',encoding = 'utf8') as file:
    readfile = csv.DictReader(file, delimiter = ',')
    for row in readfile:
        email = row["first_name"] + row["last_name"] + "@gmail.com"
        row['email'] = email
        new_employee_data.append(row)
with open('new_employee_data.csv','w',newline = '', encoding = 'utf8') as file2:
    writefile = csv.DictWriter(file2, fieldnames = ['last_name','first_name','ssn','email'])
    writefile.writeheader()
    writefile.writerows(new_employee_data)
file2.close()
        