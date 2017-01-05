import datetime

name = str(raw_input("What is your name "))

age = int(raw_input("What is your age "))


repetition = int(raw_input("Enter the number of time to  print the messages: "))

noOfYears = 100 - age

today = datetime.date.today()

currentYear =  today.year

futureYear = currentYear + noOfYears
 
print repetition * (name + " will be 100 years in " + str(futureYear) + "\n")
