text = input("Please enter a text: ")
letter_counts = {}

for letter in text:
    if letter in letter_counts:
        letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1

print(letter_counts)