# Topic 2: Data types and type()

age = 25
height = 1.83
is_student = True

print(type(age))
print(type(height))
print(type(is_student))

age_string = "25"

# This line causes a TypeError because you can't add an int and a str directly
print(age + age_string)

# Two ways to fix it:
print(age + int(age_string))   # numeric addition -> 50
print(str(age) + age_string)   # string concatenation -> "2525"