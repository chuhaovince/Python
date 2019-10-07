num = int(input("How many numbers?"))

x = 0
while x< num:
    print(x)
    x+=1
while x == num:
    ask = input("Do you want to continue?")
    if ask == "y":
        num = int(input("How many numbers?"))
        x = 0
        while x< num:
            print(x)
            x+=1
    elif ask == "n":
        break
    else:
        continue