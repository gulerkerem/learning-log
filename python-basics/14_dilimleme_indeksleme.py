cities = ["Ankara", "İzmir", "Bursa", "Antalya", "Adana"]
print(f"First city: {cities[0]} \nLast city: {cities[-1]}\nCities in the middle: {cities[1:4]}\nLast two cities: {cities[-2:]} ")

notes = [45, 82, 61, 90, 33, 77, 58]
print(f"numbers: {notes[::2]}")

word = input("Enter a word:")
if word == word[::-1]:
    print(f"Yes, the {word} is a palindrom")
else:
    print(f"No, the {word} is not a palindrom")

codes = ["TR-1001-AB", "TR-1002-CD", "TR-1003-EF", "TR-1004-GH", "TR-1005-IJ"]
middle = codes[1:4]
print(f"First code: {codes[0]} \nLast code: {codes[-1]} \nMiddle list: {middle} \nFirst code written reverse:{codes[0][-2:][::-1]} ")
for code in codes:
    print(f"Poduct numbers: {code[3:7]}")
