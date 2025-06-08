# class dummy:
#     n = 100 # class variable
#     def __init__(self):
#         print("Automatically called")
#
#     def method1(self):
#         print("method has been called")
#
# d = dummy()
# d.method1()
# print(d.n)

# class Calculator:
#     n = 100 # class variable
#     def __init__(self, a, b): # self is the instance of the class, which points to the current object, a and b are attributes
#         self.first = a # instance variable
#         self.second = b # instance variable
#         print("Automatically called")
#
#     def adding(self):
#         return self.first + self.second + Calculator.n

# d = Calculator(1, 2)
# print(d.adding())
# print(d.n) # calling class variable and its common to all objects
# print(d.first) # calling instance variable and its only for obj d

# class SmallCalculator(Calculator):
#     n2 = 100
#
#     def __init__(self, a, b):
#         super().__init__(a, b)
#
#     def small_adding(self):
#         return SmallCalculator.n2 + Calculator.n +  self.adding()
#
# d2 = SmallCalculator(1, 2)
# print(d2.small_adding())


# str
# str = "Hariharan.com"
# str1 = "Sarala"
# str3 = "haran"
#
# print(str + str1)
# print(str[0:5])
#
# var = str.split('.') # creates a list of substring separated by '.'
# print(var)
#
# str4 = " great "
# print(str4.strip()) # removes whitespaces from both the sides
# print(str4.lstrip()) # removes left white space
# print(str4.rstrip()) # deletes right white space

# class BasicCalculator:
#     def __init__(self, a, b):
#         self.a = 10
#         self.b = 5
#
#     def addition(self):
#         return self.a + self.b
#
#     def subtraction(self):
#         return self.a - self.b
#
#     def multiplication(self):
#         return self.a * self.b
#
#     def division(self):
#         return self.a / self.b
#
#
# obj = BasicCalculator(10, 5)
# print("Addition: 10 + 5 = ", obj.addition())
# print("Subtraction: 10 - 5 = ", obj.subtraction())
# print("Multiplication: 10 * 5 = ", obj.multiplication())
# print("Division: 10 / 5 = ", obj.division())

# def GreetUser(username):
#     print(f"Hello, {username}! Welcome to the Python course.")
#
#
# GreetUser('John')
#
#
# def CalculateAverage(num1, num2, num3):
#     return (num1 + num2 + num3) / 3
#
#
# print("The average of 10, 20, and 30 is", CalculateAverage(10, 20, 30))

# file = open('test.txt')
# print(file.read()) # reads the entire file
# print(file.read(10)) # vanakkam is actually 8 character, next line is 1 character, so remaining 1 character d is printed
# print(file.readline()) # reads the 1st line
# print(file.readline())  # if again called, the pointer points the 2nd line

# print line by line using WHILE loop - readline
# line = file.readline()
# while line:
#     print(line)
#     line = file.readline()

# print(file.readlines()) # returns a list of all the lines

# print line by line using FOR loop - readlines
# for line in file.readlines():
#     print(line)

# Adding content
# another way to open the file where no need to add file = open('test.txt') and file.close()
# with open('test.txt', 'r') as file:
#     print(file.read())
# we can the all the above operations again inside with

# reversing the content and printing again
# with open('test.txt', 'r') as file:
#     a = file.readlines()
#     with open('test.txt', 'w') as writer:
#         for line in reversed(a):
#             writer.write(line)

# with open('test.txt') as file:
#     c = file.read()
#     print(c)
#     # for line in file.readlines():
#     #     print(line)

# count = 0
# with open('test.txt', 'r') as file:
#     for line in file.readlines():
#         count += 1
#     print("Total number of lines:", count)

ItemsInCart = 0

def add_to_cart(items_to_add):
    global ItemsInCart
    if items_to_add < 0:
        raise Exception("Cannot add a negative number of items.")
    elif ItemsInCart + items_to_add > 5:
        raise Exception("Cart limit exceeded.")
    else:
        ItemsInCart += items_to_add
        print(f"{items_to_add} items added. Total in cart: {ItemsInCart}")

try:
    add_to_cart(2)
    add_to_cart(-1)
except Exception as e:
    print(e)