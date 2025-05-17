# # car game
# commands = ""
# started = False
# while True:
#     command = input("> ").lower()
#     if command == 'start':
#         if started:
#             print("car already started")
#         else:
#             started = True
#             print("Car started")
#     elif command == 'stop':
#         if not started:
#             print("car already stopped")
#         else:
#             started = False
#             print("Car stopped")
#     elif command == 'help':
#         print("start - to start the car\nstop - to stop the car\nquit - to exit the program")
#     elif command == 'quit':
#         break
#     else:
#         print("Invalid command")

# # for loops
# for i in 'Python':
#     print(i)
# for i in range(10):
#     print(i)
# for i in range(5,10):
#     print(i)
# for i in range(5,10,2):
#     print(i)
#
#
# # sum of list
# prices = [10, 10, 20, 30]
# tot = 0
# for i in prices:
#     tot+=i
# print(tot)
#
# # nested loops
# for x in range(3):
#     for y in range(3):
#         print(f"({x},{y})")
#
#
# # printing pattern
# #1
# numbers = [1, 2, 3]
# for i in numbers:
#     print("x" * i)
# #2
# for i in numbers:
#     count = ''
#     for x in range(i):
#         count+="x"
#     print(count)

# list
# names = ["Hari", "haran", "ram", "anish"]
# print(names) # prints list
# print(names[0]) # prints as a string
# print(names[1:])
# print(names[-1:])
# names[3] = "gopal"
# print(names)


# # list exercise - get a list of numbers and print the largest in the list
l = []
length = int(input("Enter the length of your list: "))
for i in range(length):
    add = int(input(f"Enter number {i+1}: "))
    l.append(add)
temp = l[0]
for e in l:
    if e > temp:
        temp = e
print(temp)





