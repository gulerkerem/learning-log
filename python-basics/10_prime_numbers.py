number = int(input("Please enter a number."))
prime = True
if number < 2:
      prime = False
for i in range(2, number):
    if number %i == 0:
        prime = False
        break
if prime == True:
        print(f"{number} is prime number.")
else: 
        print(f"{number} is not a prime number.")