# Prime-or-Not
#To check for first 100 numbers.
def prime_checker():
  for number in range(1,100):
    if number == 1:
      print("It's not a prime number.")
    elif number == 2 or number == 3 or number == 5 or number == 7:
      print("It's a prime number")
    elif number % 2 == 0 or number % 3 == 0:
      print("It's not a prime number.")
    elif number % 5 == 0 or number % 7 ==0:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")

prime_checker()

#If wish to get a user defined input.

def prime_checker(number):
    if number == 1:
      print("It's not a prime number.")
    elif number == 2 or number == 3 or number == 5 or number == 7:
      print("It's a prime number")
    elif number % 2 == 0 or number % 3 == 0:
      print("It's not a prime number.")
    elif number % 5 == 0 or number % 7 ==0:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")
    
n = int(input())
prime_checker(number=n)
