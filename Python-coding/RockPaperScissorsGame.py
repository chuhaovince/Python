user_input = input("Pick a shoot: P/R/S")

import random
foo = ['p','s','r']
comp_input = random.choice(foo)

if user_input == comp_input:
    print('tie')
elif (user_input == 'p' and comp_input == 's') or (user_input == 's' and comp_input =='r') or (user_input == 'r' and comp_input == 'p'):
    print('computer wins')
else:
    print('you win')
