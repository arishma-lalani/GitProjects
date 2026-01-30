# Question 4

from random import random

values = [random() for i in range(20)]
x = random()

values.sort()

first_index_that_matches_index = None
for index, value in enumerate(values):
    if value >= x:
        first_index_that_matches_index = index
        break

print("Sorted list of values: ", values)
print("The random value x is: ", x)
if first_index_that_matches_index is not None:
    print("The first index with value greater than or equal to x is: ", first_index_that_matches_index)
else:
    print("No index value in the list is greater than or equal to x")