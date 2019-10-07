# @TODO: Write a function that returns the arithmetic average for a list of numbers


# Test your function with the following:
# print(average([1, 5, 9]))
# print(average(range(11)))
import numpy as np
def average(lis):
    a = np.average(lis)
    return a

print(average((1,5,9)))
print(average(range(11)))