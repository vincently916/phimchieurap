#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
#and makes a new list of only the first and last elements of the given list. 
#For practice, write this code inside a function.

def get_list(text):
   return int(raw_input(text))

def make_list(old_list):
   new_list = [old_list[0],len(old_list) - 1]
   print new_list

number = get_list("Enter a number: ")
list = range(0,number)
make_list(list)  
