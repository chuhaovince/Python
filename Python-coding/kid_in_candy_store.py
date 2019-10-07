# The list of candies to print to the screen
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
             "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of


# Print out options

check = 'y'
while check != 'n':
    candyCart = []
    for i in candyList:
        print("[" + f'{candyList.index(i)}' + "] " + i)
    for j in range(allowance):
        user_input = input('Pick a number from 0 to 8: ')
        candyCart.append(candyList[int(user_input)])
    print("I brought home with me...")
    for i in candyCart:
        print(i)
    check = input("Do you want to pick again? (y/n)")



