#List comprehension is to condense the for loop and the list appending into one simple line
#This excercise is to write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
new = [item for item in a if item % 2 == 0]

print new
