
num = int(raw_input("Enter the first number: "))

check = int(raw_input("Enter the second number: "))


result = num % check

if result == 0: 
  print str(num) + " divides evenly by " + str(check)

else:
  print str(num) + " does not divide evenly by " + str(check)

if num % 4 == 0:
  print str(num) + " is a multiple of 4 and an even number."

elif num % 2 == 0:
  print str(num) + " is an even number."

else:
  print str(num) + " is an odd number."



