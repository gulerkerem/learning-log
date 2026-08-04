numbers = [1, -5, 2, 8, 3, -10]
for number in numbers:
    if number %2 == 0:
        print(f"{number} are Even")
    else:
        print(f"{number} are Odd")
print(len(numbers))
numbers.append("23")
print(numbers)

