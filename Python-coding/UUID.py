import string
import random

def UUID_generator(length = 4, par2 = string.digits + string.ascii_letters):
    #length = int(input(f"Please enter your UUID desired length: \n"))
    #par2 = input(f"Please enter your characters: \n")
    uuid = []
    for _ in range(length):
        uuid.append(random.choice(par2))
    return ''.join(uuid)


print(UUID_generator(7,"sl2nfs2oK2"))