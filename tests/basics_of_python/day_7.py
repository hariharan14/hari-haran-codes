
# TODO: Inheritance

# Single Inheritance - 1 parent 1 child
# class Parent:
#     def say_hello(self):
#         print("Hello from Parent")
#
# class Child(Parent):
#     pass
#
# child = Child()
# child.say_hello()

# Real life example
# class Vehicle:
#     def start_engine(self):
#         print("Engine started")
#
# class Car(Vehicle):
#     def drive(self):
#         print("Car is driving")

# Multiple Inheritance -  1 child and multiple parents
# class Mother:
#     def work(self):
#         print("Working like Mom")
#
# class Father:
#     def guide(self):
#         print("Guiding like Dad")
#
# class Child(Mother, Father):
#     pass
#
# child = Child()
# child.work()
# child.guide()

# Real life example
# class Camera:
#     def take_photo(self):
#         print("Photo taken")
#
# class Phone:
#     def make_call(self):
#         print("Calling...")
#
# class Smartphone(Camera, Phone):
#     def browse(self):
#         print("Browsing internet")


# Multilevel Inheritance - like a chain, from grandparent --> parent --> child
# simple
# class Grandparent:
#     def legacy(self):
#         print("Family legacy")
#
# class Parent(Grandparent):
#     pass
#
# class Child(Parent):
#     pass
#
# child = Child()
# child.legacy()

# with constructor, attributes, super
# class Grandparent:
#     def __init__(self, family_name):
#         self.name = family_name
#
#     def legacy(self):
#         print(f"Family legacy of {self.name}")
#
# class Parent(Grandparent):
#     def __init__(self, family_name, age):
#         super().__init__(family_name)
#         self.age = age
#
#     def gene(self):
#         print(f"From {self.name} family, being {self.age} years old")
#
# class Child(Parent):
#     pass
#
# child = Child('Doss', 20)
# child.gene()
# child.legacy()
#
# parent = Parent('Iyer', 50)
# parent.legacy()

# real life example
# class Person:
#     def walk(self):
#         print("Person is walking")
#
# class Employee(Person):
#     def work(self):
#         print("Employee is working")
#
# class Manager(Employee):
#     def manage(self):
#         print("Manager is managing")



# # Hierarchical Inheritance - Parent inherited by many child
# class Parent:
#     def skill(self):
#         print("Parent's skill")
#
# class Child1(Parent):
#     pass
#
# class Child2(Parent):
#     pass
#
# c1 = Child1()
# c2 = Child2()
# c1.skill()
# c2.skill()

# real life example
# class Employee:
#     def attend_meeting(self):
#         print("Attending meeting")
#
# class Engineer(Employee):
#     def code(self):
#         print("Engineer coding")
#
# class Designer(Employee):
#     def draw(self):
#         print("Designer drawing")


# Hybrid Inheritance - Multiple + Multilevel
# class A:
#     def dummy1(self):
#         print("A")
#
# class B(A):
#     def dummy2(self):
#         print("B")
#
# class C:
#     def dummy3(self):
#         print("C")
#
# class D(B, C):  # Combines multiple and multilevel
#     pass
#
# a = D() # a inherits all methods from A, B, C
# a.dummy1()
# a.dummy2()
# a.dummy3()

# real life example
# class Person:
#     def introduce(self):
#         print("I am a person")
#
# class Teacher(Person):
#     def teach(self):
#         print("Teaching students")
#
# class Author:
#     def write(self):
#         print("Writing a book")
#
# class Professor(Teacher, Author):
#     def research(self):
#         print("Doing research")


# TODO: Polymorphism

# run time - The correct sound method is invoked at runtime based on the actual type of the object in the list
# class Animal:
#     def sound(self):
#         print("Animal makes sound")
#
# class Dog(Animal):
#     def sound(self):
#         print("Dog woofs")
#
# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")
#
# cat = Cat()
# cat.sound()
# dog = Dog()
# dog.sound()
#
# for animal in [Animal(), Dog(), Cat()]: # Calls the appropriate method based on the object type
#     animal.sound()

# compiler time
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

# Compile-Time Polymorphism (Mimicked using default arguments)
calc = Calculator()
print(calc.add(5, 10))  # Two arguments
print(calc.add(5, 10, 15))  # Three arguments




#TODO: Method Overriding

# class Parent:
#     def show(self):
#         print("Inside Parent")
#
#
# class Child(Parent):
#     def show(self):
#         Parent.show(self)
#         super().show() # above line is same as this
#         print("Inside Child")
#
# obj = Child()
# obj.show()


# class Parent:
#     def display(self):
#         print("Inside Parent")
#
# class Child(Parent):
#     def show(self):
#         print("Inside Child")
#
# class GrandChild(Child):
#     def show(self):
#         print("Inside GrandChild")
#
# g = GrandChild()
# g.show()
# g.display()


# TODO: Operator Overloading

#1

# class A:
#     def __init__(self, a):
#         self.a = a
#
# ob1 = A(1)
# ob2 = A(2)
# ob3 = A("Geeks")
# ob4 = A("For")

# print(ob1 + ob2) # the compiler doesnt know how to add 2 objects - TypeError: unsupported operand type(s) for +: 'A' and 'A'
# print(ob3 + ob4) # the compiler doesnt know how to add 2 objects - TypeError: unsupported operand type(s) for +: 'A' and 'A'

#2 ----------------------------------------------------------

# class A:
#     def __init__(self, a):
#         self.a = a
#
#     def __add__(self, other):
#         return self.a + other.a # other is other object's(obj2) argument which is 2
#
# obj1 = A(1)
# obj2 = A(2)
# obj3 = A("Geeks")
# obj4 = A("For")
#
# print(obj1 + obj2)
# print(obj4 + obj3)
#
# # which is same as
# print(A.__add__(obj1 , obj2))
# print(A.__add__(obj3, obj4))
# #And can also be Understand as :
# print(obj1.__add__(obj2))
# print(obj3.__add__(obj4))

# 3 --------------------------------------------------------------------

# class Complex:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
# 
#     def __sub__(self, other):
#         return self.a - other.a, self.b - other.b
# 
# obj1 = Complex(4, 5)
# obj2 = Complex(1, 2)
# 
# print(obj1 - obj2)
# print(Complex.__sub__(obj1, obj2))
# print(obj1.__sub__(obj2))

# 4 ------------------------------------------------------------------------

# using all the magic operators

# class AllMagic:
#     def __init__(self, a):
#         self.a = a
#
#     def __add__(self, other):
#         return self.a + other.a
#
#     def __sub__(self, other):
#         return self.a - other.a
#
#     def __mul__(self, other):
#         return self.a * other.a
#
#     def __truediv__(self, other):
#         return self.a / other.a
#
#     def __floordiv__(self, other):
#         return self.a // other.a
#
#     def __mod__(self, other):
#         return self.a % other.a
#
#     def __and__(self, other):
#         return self.a & other.a
#
#     def __xor__(self, other):
#         return self.a ^ other.a
#
#     def __or__(self, other):
#         return self.a | other.a
#
#     def __lt__(self, other):
#         return self.a < other.a
#
#     def __le__(self, other):
#         return self.a <= other.a
#
#     def __eq__(self, other):
#         return self.a == other.a
#
#     def __ne__(self, other):
#         return self.a != other.a
#
#     def __ge__(self, other):
#         return self.a >= other.a
#
#     def __gt__(self, other):
#         return self.a > other.a
#
# x = AllMagic(10)
# y = AllMagic(3)
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x // y)
# print(x % y)


# TODO: Encapsulation
class Dog:
    def __init__(self, name, breed, age):
        self.name = name  # Public attribute
        self._breed = breed  # Protected attribute
        self.__age = age  # Private attribute

    # Public method
    def get_info(self):
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"

    # Getter and Setter for private attribute
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")

# Example Usage
dog = Dog("Buddy", "Labrador", 3)

# Accessing public member
print(dog.name)  # Accessible

# Accessing protected member
print(dog._breed)  # Accessible but discouraged outside the class

# cant access since Hidden from outside, Getter/SetterMethods to read or update private data
print(dog.__age)

# Accessing private member using getter
print(dog.get_age())

# Modifying private member using setter
dog.set_age(5)
print(dog.get_info())

#2
class Student:
    def __init__(self, name, grade):
        self.__name = name       # private variable
        self.__grade = grade     # private variable

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, new_name):
        if isinstance(new_name, str) and new_name != "":
            self.__name = new_name
        else:
            print("Invalid name!")

    # Getter for grade
    def get_grade(self):
        return self.__grade

    # Setter for grade
    def set_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
        else:
            print("Invalid grade! Must be between 0 and 100.")

s = Student("Alice", 85)

print(s.get_name())    # ✅ Alice
print(s.get_grade())   # ✅ 85

s.set_name("Bob")      # ✅ Changing name
s.set_grade(95)        # ✅ Changing grade

print(s.get_name())    # ✅ Bob
print(s.get_grade())   # ✅ 95

s.set_grade(120)       # ❌ Invalid grade

# TODO: Abstraction
# Import required modules
# from abc import ABC, abstractmethod
#
#
# # Create Abstract base class
# class Car(ABC):
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#     # Create abstract method
#     @abstractmethod
#     def printDetails(self):
#         pass
#
#     # Create concrete method
#     def accelerate(self):
#         print("Speed up ...")
#
#     def break_applied(self):
#         print("Car stopped")
#
#
# # Create a child class
# class Hatchback(Car):
#     def printDetails(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Year:", self.year)
#
#     def sunroof(self):
#         print("Not having this feature")
#
#
# # Create a child class
# class Suv(Car):
#     def printDetails(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Year:", self.year)
#
#     def sunroof(self):
#         print("Available")
#
#
# # Create an instance of the Hatchback class
# car1 = Hatchback("Maruti", "Alto", "2022")
#
# # Call methods
# car1.printDetails()
# car1.accelerate()
# car1.sunroof()

# 2 - simpler
# from abc import ABC, abstractmethod
#
# class Dog(ABC):  # Abstract Class
#     def __init__(self, name):
#         self.name = name
#
#     @abstractmethod
#     def sound(self):  # Abstract Method
#         pass
#
#     def display_name(self):  # Concrete Method
#         print(f"Dog's Name: {self.name}")
#
# class Labrador(Dog):  # Partial Abstraction
#     def sound(self):
#         print("Labrador Woof!")
#
# class Beagle(Dog):  # Partial Abstraction
#     def sound(self):
#         print("Beagle Bark!")
#
# # Example Usage
# dogs = [Labrador("Buddy"), Beagle("Charlie")]
# for dog in dogs:
#     dog.display_name()  # Calls concrete method
#     dog.sound()  # Calls implemented abstract method
