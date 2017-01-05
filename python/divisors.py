
number = int(raw_input("Enter a number: "))
x = range(2,number)
divisors = []
for each in x:
 if number % each == 0:
    divisors.append(each)

print "list of divisors: ", divisors


