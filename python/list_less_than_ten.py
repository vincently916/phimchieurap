check = int(raw_input("Enter a number: "))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list = []
for num in a:
  if int(num) < check:
     list.append(num)

print list   
 
