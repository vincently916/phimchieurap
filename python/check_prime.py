#Ask the user for a number and determine whether the number is prime or not.
#A prime is a number that has no divisors

def get_number(text):
   return int(raw_input(text))

def check_prime(num):
   for divisor in range(2,num):
      if num % divisor == 0: 
          return False 


number = get_number("Enter a number: ")

isPrime = check_prime(number)

if isPrime == "true":
  print str(number) + " is not a prime."
else:
  print str(number) + " is a prime."
