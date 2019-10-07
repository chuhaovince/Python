pies = ['Pecan','Apple Crisp','Bean', 'Banoffee', 'Black Bun', 'Blueberry',
        'Buko','Burek','Tamale', 'Steak']

print("Welcome to the House of Pies! Here are our pies\n\n")

print("------------------------------------------------------------------------------")
for i in pies:
    print("(" + f'{pies.index(i)+1}' + ") " + i, end = " ")

print('\n')
check = 'y'
num_pies = 0
pies_purchased = []
while check == "y":
    choose = input("Choose a pie by number: ")
    print("Great! We'll have that " + pies[int(choose)-1] + " right out for you")
    num_pies +=1
    pies_purchased.append(pies[int(choose)-1])
    check = input("do you want to continue? y/n")
print(f'Total number of pies ordered is {num_pies}')
print(f'You purchased:')
for i in pies:
    if i in pies_purchased:
        print (f'{pies_purchased.count(i)}' + " " + i)
    else:
        print(str(0) + " " + i )
     

