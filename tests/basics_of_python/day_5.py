# TODO: Class
# class Point:
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
# point = Point()
# point.move()
# point.draw()
# point.x = 10
# point.y = 20
# print(point.x)
# print(point.y)
# point2 = Point()
# # print(point2.x) #attribute error, x and y are attributes of only point, each object has different instances of the Point class

# TODO: Constructor
# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print("move")
#
# point = Point(1,2)
# print(point.x, point.y)
# point.x = 3
# print(point.x, point.y)

# TODO: Task to create a new type person with name attribute and talk method
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f"Hi {self.name} please talk")
#
# person1 = Person("Hari")
# person1.talk()
# person1.name = "Sai"
# person1.talk()
#
# person2 = Person("Sri")
# person2.talk()

# TODO: Inheritance
# class Dog:
#     def walk(self):
#         print("walk")
#
#
# class Cat:
#     def walk(self):
#         print("walk")
#
# # to avoid duplicates we'll inherit the class to get access to all the methods of the parent class
# class Mammals:
#     def walk(self):
#         print("walk")
#
#
# class Dogs(Mammals):
#     pass
#
#
# class Cats(Mammals):
#     def eat(self):
#         print("eat")
#
#
# dog = Dog()
# dog.walk()
# cat = Cats()
# cat.walk()
# cat.eat()


# TODO: Modules
# import utils
#
# print(utils.kg_to_lbs(10))
#
# from utils import lbs_to_kg
#
# print(lbs_to_kg(100))

# TODO: Task for creating a max number finding function in utils and call it here
# from utils import *
#
# r = int(input("Enter the range of list: "))
# a = []
# for i in range(r):
#     add = int(input(f"Enter number {i+1}: "))
#     a.append(add)
# # print(find_max(a))
# print(find_max_2(a))

# TODO: Packages
# #1
# import local_venv.utils_2
# #2
# from local_venv.utils_2 import find_max_2
# #3
# from local_venv import utils_2

# r = int(input("Enter the range of list: "))
# a = []
# for i in range(r):
#     add = int(input(f"Enter number {i+1}: "))
#     a.append(add)

# #1
# local_venv.utils_2.find_max_2(a, r)
# #2
# find_max_2(a, r)
# #3
# utils_2.find_max_2(a, r)




# TODO: Random numbers
# import random

# members = ['Hari', 'sai', 'sri']
# for i in range(5):
    # print(random.random())
    # print(random.randint(20, 100))
    # print(random.choice(members))

# TODO: Task to create a class which has a method dice which will print a tuple of random numbers from a dice
#1
# import random
#
# class Dice:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def roll(self):
#         # print(f"({self.x}, {self.y})")
#         return self.x, self.y # if we return without any brackets, it will return as a tuple
#
#
# t = Dice(random.randint(1, 6), random.randint(1, 6))
# # t.roll()
# print(t.roll())

#2
# import random
#
# class Dice:
#     def roll(self):
#         first = random.randint(1,6)
#         second = random.randint(1,6)
#         return first, second
#
#
# okay = Dice()
# print(okay.roll())


