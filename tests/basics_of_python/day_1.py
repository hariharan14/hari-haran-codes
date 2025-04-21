"""
# string concatenation
name = input("What's your name? ")
color = input("What's your favorite color? ")
print(name + " likes " + color)

# type conversion
birth_year = input("What's your birth year? ")
print(type(birth_year))
age = 2025 - int(birth_year)
print(type(age))
print(age)

pounds = input("How many pounds do you have? ")
print(type(pounds))
kg = int(pounds) * 0.4
print(type(kg))
print(kg)

# string types
double = "Python's course for "
single = '"beginners"'
print(double + single)


# String indices
a = 'Python for beginners'
print(a)
print(a[1:13])
print(a[2:])
print(a[:-2])
print(a[1:-1])
print(a[:6])
print(a[:])
another = a[:]
print(another)

#formatted strings
first = 'Hari'
last = 'haran'
# exp output - Hari [haran] is a coder
message = first + ' [' + last + '] is a coder.' #bad
msg = f"{first} [{last}] is a coder."
print(message)
print(msg)

# string methods
course = 'Python for Beginners'
print(len(course)) # print and len general built-ins
print(course.upper()) # all caps
print(course.lower()) # all small
print(course.title()) # 1st letter of each word caps
print(course.find('P')) # 0
print(course.find('Beginners')) # 11
print(course.find('For')) # -1 if it cant find (case-sensitive)
print(course.replace('Python', 'Java'))
print(course.replace('python', 'Java')) # prints the old str if it cant find (case-sensitive)
print("Python" in course) # bool
print("Java" in course) # bool

# arithmetic operators
# operators precedence - ().....**.....* or / or //.....+ or - or % .....(left to right if same precedence)
x = 5 + 6 - 1 * 5 ** 2 / 2
print(x)
print((10 // 3) % 2 ** 0 + 1 / 2)
"""
