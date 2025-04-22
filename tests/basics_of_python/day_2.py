import math

# x = -2.9
# print(round(x)) # -3
# print(abs(x)) # 2.9

# Math module - methods
x = 5.1
y = 5.9
# print(math.ceil(x)) # 6
# print(math.floor(y)) # 5
# print(math.exp(x)) # 164.0219072999017 (e ** x)
# print(math.factorial(x)) # fails as we cant find fact of float (ValueError: factorial() only accepts integral values)
# print(math.factorial(4)) # 4*3*2*1 = 24
# print(math.fabs(x-y)) # 0.8
# print(math.isclose(x,y)) # False
# print(math.isclose(1.233, 1.24)) # False
# print(math.isclose(1.233, 1.233000001)) # True (minute diff, exactly same number also true)
# print(math.isfinite(23555555555555.77777777777777777)) # True
# print(math.isinf(math.pi)) # False (pi is limited to some digits making it finite)
# print(math.sqrt(10)) # 3.1622776601683795
# print(math.isqrt(10)) # 3
# print(math.pow(3, 2)) # 9.0
# z = (3, 3, 4.0)
# print(math.prod(z)) # 36.0
# print (math.remainder(23.5, 5.5)) # 1.5
# print (math.remainder(23.5, 5)) # -1.5
# print (math.remainder(11, 2)) # -1.0
# print (math.remainder(9, 2)) # 1.0
# print (math.remainder(9, 5)) # -1.0
# print(math.trunc(math.tau)) # 6

# # IF statement
# price = 1000000
# has_good_credit = True
# if has_good_credit:
#     down_pay = 0.1 * price
# else:
#     down_pay = 0.2 * price
# print(f"Down payment: ${down_pay}")

# # Logical operator - and, or, not
# has_high_income = True
# has_good_credit = True
# has_criminal_records = False
# if has_high_income and has_good_credit:
#     print("Eligible for loan")
# if has_good_credit and not has_criminal_records:
#     print("Eligible for loan")
# has_good_credit = False
# if not has_good_credit or has_criminal_records:
#     print("Not Eligible for loan")

# # Comparative operators
# name = input("Enter name: ")
# if len(name) < 3:
#     print("Please enter more than 3 character")
# elif len(name) > 50:
#     print("Please enter more than 50 character")
# else:
#     print("sounds good")

# # Project: Weight convertor
# weight = int(input('Weight: '))
# unit = input("(L)bs or (K)g: ")
# if unit.lower() == 'l':
#     print(f"You are {weight * 0.453592} Kilograms")
# elif unit.lower() == 'k':
#     print(f"You are {weight * 2.20462} Pounds")
# else:
#     print("Enter a valid unit")

# # While loop
# i = 1
# while i <= 5:
#     print(i)
#     i+=1
# print("Done")
#
# i = 5
# while i > 0:
#     print('*' * i)
#     i-=1
# print('Done')

# # while guessing game - old
# i = 0
# while i < 3:
#     number = int(input('Guess: '))
#     if number == 5:
#         print("You win")
#         break
#     elif number != 5:
#         i+=1
#         continue
# if i > 2:
#     print("Sorry u failed")
#
# # while guessing game - better
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print("You won")
#         break
# else:
#     print("Sorry u failed")

