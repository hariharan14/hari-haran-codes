# TODO: 2D Arrays
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix[2][2])
# matrix[1][1] = 7
# print(matrix[1][1])
# for row in matrix:
#     for i in row:
#         print(i)

# TODO: List Methods
# n = [5, 4, 3, 5, 2, 3, 2]
# n2 = n.copy()

# print(n.append(8)) # usually returns none, but the operation wud have been completed, just print the list again and check
# print(n)
#
# n.insert(4, 9) # inserts the obj in the provided index
# print(n)
# print(n.index(9))

# n.remove(2) # removes the obj from the list, if multiple times the obj is present, it removes the 1st occ of the obj
# print(n)

# n.clear()
# print(n)

# n.pop() # removes the last obj
# print(n)

# print(n.index(5)) # finds index of the obj in the 1st occurrence, used to find if the obj is present in the list, if its not there, error comes, so better to use the below 'in' operator

# print(3 in n)
# print(50 in n)

# print(n.count(5)) # counts the no. of occ in the list

# n.sort() # sorts in ascending order
# print(n)
# n.reverse() # to sort in reversing order, usually the list is sorted 1st and then reversed
# print(n)

#TODO: Task to remove duplicates
#1
# n = [5, 4, 3, 5, 2, 3]
# for i in n:
#     if n.count(i) > 1:
#         n.remove(i)
# print(n)
#
# #2
# numbers = [5, 4, 3, 5, 2, 3]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

# Tuples
# n = (1, 2, 3, 4, 5, 2)
# print(n.count(2))
# print(n.index(2)) # only 2 methods
# n[1] = 3
# print(n) # type error

# Unpacking
# c = (1, 2, 3)
# x = c[0]
# y = c[1]
# z = c[2]
# print(x*y*z)
#
# x, y, z = c
# print(x*y*z)

# Dictionary
customer = {
    "name": "Hari",
    "age": 22,
    "Phone": 1234,
    # 'age': 22 # key shud be unique in a dict
}
# print(customer["name"])
# # print(customer["sex"]) #key error
# # print(customer["Age"]) #key error
# print(customer.get("name"))
# print(customer.get("birth year"))
# print(customer.get("birth year", 2000))
#
# customer.pop("name")
# print(customer)
#
# customer['age'] = 25 # modifying
# customer['birth year'] = 2000 # adding new pair
# print(customer)

#TODO: phone number printing in words

# words = {
#     1: "One",
#     2: "Two",
#     3: "Three",
#     4: "Four",
#     5: "Five",
#     6: "Six",
#     7: "Seven",
#     8: "Eight",
#     9: "Nine",
#     0: "Zero",
# }
# n = input("Phone: ")
# count = ""
# for i in n:
#     count+=words.get(int(i), "!") + " "
# print(count)

# TODO: Emoji convertor
# x = input("> ")
# x = x.split(" ")
# print(x)
# emoji = {
#     ":)": "😊",
#     ":(": "😒"
# }
# count = ""
# for i in x:
#     count += emoji.get(i, i) + " "
# print(count)


# TODO: Functions

# def greet_user():
#     print("Hi there!")
# print('start')
# greet_user()
# print('end')

# parameters
# def greet_user(name):
#     print(f"Hello {name}")
# greet_user('Hari')
# # greet_user() #type error
#
# # keyword arguments
# def parent_names(father, mother): #here father and mother are parameters
#     print(f"Father name: {father}\nMother name: {mother}\n")
# print("Parental information:")
# parent_names("Murugesan", "Sarala") # murugesan and sarala are positional arguments
# parent_names("Sarala", "Murugesan") # wrong way
# parent_names(mother="Sarala", father="Murugesan")   # mother=, father= are keyword arguments
# # parent_names(mother="Sarala", "Murugesan") # always keyword arguments comes after positional arguments
# # parent_names("Sarala", father="Murugesan") # type error saying multiple argument father(to interchange the position of the argument use keyword arguments in all places and do not use both)
# parent_names("Murugesan", mother="Sarala") # correct way

# TODO: Return statement

# def square(n):
#     print(n*n)
# print(square(2)) #prints value and what the function returns which is None by default
#
# #therefore using return to return something from function instead of None
# def square(n):
#     return n*n
# print(square(3))


# reusable function - emoji convertor

# def emoji_convertor(message):
#     command = ""
#     emoji = {":)": "😊", ":(": "😒"}
#     words = message.split(" ")
#     for word in words:
#         command += emoji.get(word, word) + " "
#     return command
#
# message = input("Enter: ")
# print(emoji_convertor(message))


# TODO: Exceptional handling

# age = int(input("Enter your age: "))
# print(age) #if we enter some string, it will fail with value error

# so handling the particular exception
# try:
#     age = int(input("Enter your age: "))
#     print(age)
# except ValueError:
#     print('Invalid input')

# handling various exceptions with diff exception block - ZeroDivisionError comes
# try:
#     age = int(input("Enter your age: "))
#     income = 20000
#     risk = income / age
#     print(age)
# except ValueError:
#     print('Invalid input')

# handling ValueError and ZeroDivisionError
# try:
#     age = int(input("Enter your age: "))
#     income = 20000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print("Enter age greater than 0")
# except ValueError:
#     print('Invalid input')






