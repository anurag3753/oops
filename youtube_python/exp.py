# with open("demo.txt", "a") as fh:
#     for i in range(10):
#         fh.write(f"this is line {i+1} \n")


# sample iterator
# from dataclasses import dataclass


# class Node:
#     def __init__(self, data) -> None:
#         self.data = data
#         self.next = None

#     def append(self, head, node):
#         self.head.next = node

#     def __str__(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end = "")
#         print("\n")

#     def __iter__(self):
#         return self

#     def __next__(self):
#         pass


# head = Node(1)

# import argparse

# if __name__ == "__main__":
#     # Initialize the parser
#     parser = argparse.ArgumentParser(
#         description = "My demo script"
#     )

#     # Add the parameters positional/optional
#     parser.add_argument("num1", help="Number 1", type=float)    # positional parameters
#     parser.add_argument("num2", help="Number 2", type=float)
#     parser.add_argument("-o", "--operation", help="provide operator", default="+") # optional parameters (--)
#     parser.add_argument("-p", "--pass", help="provide operator", default="+") # optional parameters (--)

#     # Parse the arguments
#     args = parser.parse_args()
#     print(args)
#     if args.operation == "+":
#         print(args.num1 + args.num2)

# my_list = [1,2,3,4,5]

# # map syntax : map(function, iterable)
# ans = map(lambda x : x * 2, my_list)

# my_list = [1,2,3,4,5]
# my_list2 = [6,7,8,9,10]

# # ans = map(lambda x, y : x + y, my_list, my_list2)
# # print(list(ans))

# # my_list = [4,8,1,3,7]
# # c = filter(lambda x: True if x > 5 else False, my_list)
# # print(list(c))
# from functools import reduce
# my_list = [4,8,1,3,7]
# e = reduce(lambda x, y : x + y, my_list)
# print(e)


# my_list = [4,8,1,3,7]
# e = map(lambda x, y : x + y, my_list, my_list2)
# print(list(e))

# def nth_power(exponent):
#     def pow_of(base):
#         return pow(base, exponent)
#     return pow_of

# square = nth_power(2)
# print(square(16))


# def decorator_X(func):
#     def wrapper():
#         print("X"*20)
#         func()
#         print("X"*20)
#     return wrapper

# def decorator_Y(func):
#     def wrapper():
#         print("Y"*20)
#         func()
#         print("Y"*20)
#     return wrapper

# @decorator_Y
# @decorator_X
# def say_hello():
#     print("hello_world")

# say_hello()
from time import time
def timing(func):
    def wrapper(*args, **kwargs):
        start = time()
        print(f"start : {start}")
        result = func(*args, **kwargs)
        end = time()
        print(f"end : {end}")
        print(f"Time Elapsed : {end-start}")
        return result
    return wrapper

@timing
def my_func(li):
    _sum = 0
    for ele in li:
        _sum += ele
    return sum

a = list(range(2000000))
my_func(a)