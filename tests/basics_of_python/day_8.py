# import math
#
# n = 3.7
# print(math.floor(n))
# print(math.ceil(n))

# x = lambda a : a + 10
# print(x(5))

# n = [1, 2, 3, 4]
# print([val ** 2 for val in n])

# def fun(*args):
#     for arg in args:
#         print(arg)
#
# fun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# t = (1, 2)
# print(type(t))
#
# d = {2: 'b', 'a': 1}
# print(d)

# def fun(max):
#     cnt = 1
#     while cnt <= max:
#         yield cnt
#         cnt += 1
#
# ctr = fun(5)
# for n in ctr:
#     print(n)

def fun():
    yield 1
    yield 2
    yield 3

ctr = fun()
print(next(ctr))
print(next(ctr))
print(next(ctr))

