numbers = []
for i in range(5):
    number = int(input("Enter a number."))
    numbers.append(number)

print(f"biggest number : {max(numbers)}")
print(f"smallest number : {min(numbers)}")