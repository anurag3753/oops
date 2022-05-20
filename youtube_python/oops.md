# FrozenSets
One big reason for using frozenset is that you can use it as a key in a hashable structures (like dictionary). In most cases you could use tuple for that purpose, but sometimes you can’t know what the order of the entries will be. In that case frozenset is a great help, because it is unordered. So, for instance, a pair ‘a, b’ is treated as the same as ‘b, a’. And sometimes it is exactly what you need

# List Comprehension
- newList = [ expression(element) for element in oldList if condition ] 

# Procedural Vs Object Oriented ?
- unit - function
- concentrates on creating functions
- data and operations in the data are separated

- unit - class
- concentrates on creating classes and then these classes have data and member functions inside it.
- data and operations on it are tied together.
- A class refers to as a blue print in which we can have data and methods together.
- instance of class (It combines data and methods together)
- An object is able to store state of some kind
- Even though we have already declared the class. Post that also we can add attributes to class objects.
- pass keyword represents an empty operation
- We added init method to the class, it serves as constructor for the class. self is usually the first argument of the init keyword. this is the first method that is called whenever we create a class object.
- init is closest thing to a constructor. Even though it is not a constructor. Python does not have a destructor also. Even though other programming languages have destructor also.
- self is essentially the current object. It is similar to using `this` in c++/java. 
- It is convention to use `self` keyword to indicate that this is the current object. Even though we can use other variable names too.
- self is automatically passed when we initialize a class. So the below syntax will throw error as:
```python
class Hello:
    def __init__():
        pass
```python
# create its object
hello = Hello()    # Will throw error as init takes 0 positional args but 1 was given

- Can we create multiple init method in class
- It is not possible to provide multiple init method in python class. init method which is defined in the last will be considered as the main init method and other will be overridden
- How do I create instances with variable number of args

def __init__(self, name, suname=""):
    pass

We can create objects now as :

hello = Hello("anurag")
hello2 = Hello("anurag", "modi")

def __init__(self, *args):
    pass

It receives tuple as an argument and hence we can supply it multiple values at the same time.

Encapsulation :- It is useful, when you need to provide your code to others. And you want to protect the misuse of your code. Restricting the data access using getters and setters is called Encapsulation

Variables :-
    
def __init__(self):
    self.a = 10
    self._b = 20
    self.__c = 30

print(self.__c) Not able to access outside class. In python it is convention to use this syntax for a private variable.
print(self._b) :- It means it is a partially private variable and it is only a convention

A private member variable is private to the class. That means we can use it freely inside the class, but outside the class it is not accessible. Or accessible only through getters and setters.

# Private method inside class
```python
class Hello:
    def __init__(self):
        pass
    
    def __private_method(self):
        print("I am only callable inside class")

    def public_method(self):
        print("I can call private method, bcz i am part of class")
        self.__private_method()
```

# Inheritance
- classes in python can be extended, creating new classes which retain characteristics of the base class
- this process is known as inheritance
- Involves a superclass and a subclass
- The subclass inherits the members of the superclass and on top of it adds its own members
- subclasses have `is-a` relationship with superclass
- We can not inherit the private variables from superclass to subclass

```python
class Polygon:
    __width = None        # private vars can not be inherited
class Triangle(Polygon):
    def print(self):
        print(self.__width)    # Throws error

# Solution is to provide access of private var using getter and setters (defined as public member functions)
class Polygon:
    __width = None

    def get_width(self):
        return self.__width

class Triangle(Polygon):
    def print(self):
        print(self.get_width)    # Will be able to access the width value
```

# Modules in python
- A module is nothing but a python file.
- Exercise : Create 2 python files (utils.py, test.py) at same level
- In test.py, we can write below line
```python
# test.py
import utils    # All functions from utils will be available to use in test
```
# More points
- dir/utils.py
- test.py
- Then we can use below syntax as well
```python
from dir import utils     # Relative import
import dir.utils as du    # Relative import sequence
# Since it is getting accessed from the same path, so no problem
```
# Multiple inheritance
- Ability of a class to inherit from more than one class
```python
class Rectangle(Polygon, Shape):
    pass                # It is inheriting from two classes Polygon and Shape
```

# super keyword
```python
class Parent:
    def __init__(self):
        print("Parent __init__")

class Child(Parent):
    def __init__(self):
        print("Child __init__")

child = Child()    # child init will be executed
print(child.__class__.__mro__)    # To get the method resolution order for inherited classes
```

## Multiple Inheritance MRO
```python
class Parent:
    def __init__(self, name):
        print("Parent __init__", name)

class Parent2:
    def __init__(self, name):
        print("Parent2 __init__", name)

class Child(Parent2, Parent):
    def __init__(self):
        print("Child __init__")
        super().__init__("anurag")    # But it will lead to only calling of only Parent2 init function, what if you want to call Parent init as well.

# To call parent init as well, we need to use class names instead of super
class Child(Parent2, Parent):
    def __init__(self):
        print("Child __init__")
        Parent2.__init__(self, "anurag")     # Notice the `self` keyword is also provided here
        Parent.__init__(self, "akash") 

child = Child()    # child init will be executed
print(child.__class__.__mro__)    # To get the method resolution order for inherited classes
```

# Composition and Aggregation
- These two are related concepts, but different ways to represent the same thing
- Composition
    - In composition, the classes which have some relationships, is represented by keyword `part-of`
    - As soon, as we delete an instance of employee class, instance of salary will also be deleted
    - Book class and Chapter class. A book is not a chapter and a chapter is not a book
    - We can delegate some responsibilities from a book class to the chapter class
    - In composition, salary and employee classes are interdependent on each other

- Aggregation
    - In composition, the classes which have some relationships, is represented by keyword `has-a`
    - Ex. Employee has a salary
    - Both object are independent of each other. If one object dies, that does not mean other object will also die
    - Associated classes have unidirectional association. We are passing salary to employee class and not the vice-versa

```python
class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
    def annual_salary(self):
        return (self.pay*12) + self.bonus

# Composition    (part of relationship) [Salary is part of employee] (salary can not exist w/o employee)
# composition also means we are delegating some responsibilities from one class to another class
class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.obj_salary = Salary(pay, bonus)    # instantiating salary class inside employee class

    def total_salary(self):
        return self.obj_salary.annual_salary()

# client code for composition
emp = Employee("Anurag", 30, 100, 10)
print(emp.total_salary())
#--------------------------------------------------#
# Aggregation (Has a relationship) (Employee has a salary)
class Employee:
    def __init__(self, name, age, salary):    # salary class is passed here
        self.name = name
        self.age = age
        self.obj_salary = salary              # Getting the salary to salary object

    def total_salary(self):
        return self.obj_salary.annual_salary()

# client code for composition
salary = Salary(100, 10)
emp = Employee("Anurag", 30, salary)
print(emp.total_salary())
```

# Abstract classes
- I do not want to allow users to create an instance of Shape class
- I want, methods defined in shape class to be implemented inside the other classes inheriting it
- Solution is to use Abstract Class

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): pass
    
    @abstractmethod
    def perimeter(self): pass

class Square(Shape):
    def __init__(self, side):

```

# Exception
- An exception is an event, which occurs during the execution if a program, that disrupts the normal flow of the program
- ZeroDivisionError, TypeError, NameError, AttributeError (Ex, x.ab())
- You need to use multiple except statements to catch multiple types of exceptions
```python
import builtins
help(builtins)
```

# Try-Except-Finally
```python
try:
    statements # statements that can raise exceptions
except:
    statements # statements that will be executed to handle exceptions
else:
    statements # statements that will be executed if there is no exception
finally:
    statements # it will be executed no matter what

try:
    age=int(input('Enter your age: '))
except:
    print ('You have entered an invalid value.')
else:
    if age <= 21:
        print('You are not allowed to enter, you are too young.')
    else:
        print('Welcome, you are old enough.')
```
- finally use case 
    - (to handle the database connection lost state, you can write code to reconnect the db in this scenario)
    - (you opened a file, and started reading it, while reading you faced some error, it is always needed to close the file)

```python
try:
    statements
finally:
    statements
# We can have try and finally statements, as these statements will always execute no matter what
```

# Use of raise
- raise is similar to throw in java/c++.
- It allows programmer to raise a specific kind of exception to occur
- Like if someone wants to update salary. Then he provides -ve salary as i/p, then we can raise our exception like salary can not be -ve
- Always raises specific errors

# Raising Custom Exception
```python
class CoffeeTooHotException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class CoffeeTooColdException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class CoffeeCup:
    def __init__(self, temperature):
        self.__temperature = temperature

    def drink_coffee(self):
        if self.__temperature > 85:
            raise CoffeeTooHotException(f"Coffee Temperature : {self.__temperature}")
        elif self.__temperature < 65:
            raise CoffeeTooColdException(f"Coffee Temperature : {self.__temperature}")
        else:
            print("Coffee ok to drink")
```

# Idea behind __name__ == __main__
- 2 files utils.py, test.py
```python
# utils.py
def add (a, b):
    return a + b
print(add(10, 16))

# test.py
import utils
print(utils.add(3,5))

## o/p
26            # This is side-effect coming from importing the utils module. As while importing the utils module it is executing all the statements inside it.
8
```
- __name__ : It is a special builtin, whose value is either equal to __main__ or the module name (python filename) in which it is defined
- whenever we runs, utils.py as main python file. Then __name__ is set to __main__
- whenever we import it, and use it in some other file, then __name__ is set to the module name
- So, do not leave stray statements in imported files, they will be executed when you import that module

# Read and Write files in python
```python
with open("demo.txt", "w") as fh:    # will create the file, if it does not exist. IF exist it will overwrite its contents
    fh.write("I am a good person \n I am working on DS and Algo \n I already read sliding window")

with open("demo.txt", "a") as fh:
    for i in range(10):
        fh.write(f"this is line {i+1}")

with open("demo.txt", "r") as fh:
    print(fh.read())    # dumps the entire file contents

# If I just need to read the first 4 characters of the file then I can mention this info as

print(fh.read(4))        # It will read the first 4 characters
print(fh.readline())     # It will help in reading the complete line
print(fh.readline(4))    # It will read first 4 char of that line
```
# Read all lines in form of a list
```python
li = []
with open("demo.txt") as fh:
    li = fh.readlines()    # return all lines in form of a list
```
# Read all lines one by one
```python
with open("demo.txt") as fh:
    for line in fh:
        print(line.strip())
```

# Handle JSON data in python
- It is a text format. It stands for Javascript Object Notation. It is used for storing and exchanging data
- We can provide majority of collections to this dumps function
```python
import json

a = {
    "name" : "anurag,
    "age" : 22,
    "marks" : [90,50,30,80],
    "pass" : True
}
# to convert this python dict to json, we use json.dumps
print(json.dumps(a, indent=4))
print(json.dumps(a, indent=4, sort_keys=True))
json.dumps(list)
json.dumps(tuple) #string, int, float, boolean, None
# set can not be provided, other than sets we can provide everything

## Saving data to a json file
with open("demo.json", "w") as fh:
    fh.write(json.dumps(a, indent=2))

```
## Read from JSON
```python
import json

with open("demo.json", "r") as fh:
    json_str = fh.read()
    json_value = json.loads(json_str)    # to convert a json string value to a python dict
    print(type(json_value))    # it returns a python dict
```

# Iteration
- An act of going over a collection is called an iteration
- Collections like list, tuple, dictionary, sets

# Iterator
- Iterator is an object which can be used to iterate over a collection. Iterator object has two special methods __iter__() and __next__().
- __iter__() : It gives use the iterator
- __next__() : It gives us the next value using the iterator
```python
a = [1,2,3,4,5]
dir(a) # It gives you the methods and variables available for that object
it = iter(a)    # create an iterator over list
next(it)    # will o/p 1
next(it)    # will o/p 2
# Finally raises StopIteration exception
```

## Custom Iterator Class
```python
class ListIterator:
    def __init__(self, list):
        self.__list = list
        self.__index = -1
    
    def __iter__(self):
        return self

    def __next__(self):
        self.__index += 1
        if self.__index >= len(self.__list):
            raise StopIteration
        return self.__list[self.__index]

# client code
a = [1,2,3,4,5]
mylist = ListIterator(a)
it = iter(mylist)
print(next(it))
print(next(it))
print(next(it))

# We can also use for loop with iterators
for i in it:
    print(i)
```

# Generators
- Generators are simple ways to create an iterator.
- A generator is a function that returns an iterator object on which we can iterate upon.
- Just as iterators, generators also follow lazy evaluation
```python
def my_fun():
    # if function contains at least one yield keyword, then this function is called a generator function
    yield 'a'
    yield 'b'
    yield 'c'

# Basically yield keyword saves the status of the function after returning its value. Kind of pauses the function, with complete function state saved.

x = my_func()
```
## Difference between yield and return
- in case return the execution is terminated entirely. You can not do anything inside a function once you encountered a return statement
- But yield keyword pauses the function and save its state
- We can use next keyword in a generator function
- Generator functions returns an iterator object
- It is like using the iterator but much easier to use. We just need to use the yield keyword, instead of implementing the iter and next method inside your class
- Generators are similar to iterators, but they are more simpler to use and create.
- Generators takes care of throwing stopiteration exception as well.
- In case of generators iter and next are auto implemented for us.

## Python yield vs return
- The return statement returns the value from the function and then the function terminates. 
- The yield expression converts the function into a generator to return values one by one.
- Python return statement is not suitable when we have to return a large amount of data. 
- In this case, yield expression is useful to return only part of the data and save memory.


```python
# This generator code is synonymous to above class ListIterator code
def list_iterator(list):
    for i in list:
        yield i

# client code
a = [1,2,3,4,5]
mylist = list_iterator(a)
#it = iter(mylist)    # Not needed now
# print(next(it))
# print(next(it))
# print(next(it))
print(next(mylist))    # generator auto returns an iterator object
```

# Advantages of using generators
- Generators are easy to implement
- Generators are more efficient, as compare to normal function
- Generators are memory efficient, they do not store all values. They work on these values one by one
- Lets say, you have a stream of numbers coming in. Then with generators you do not need to wait till the entire stream comes.
- It can auto start working on the stream data as soon as they start coming
- Like read a large text file

# argparse
```python
import argparse

if __name__ == "__main__":
    # Initialize the parser
    parser = argparse.ArgumentParser(
        description = "My demo script"
    )

    # Add the parameters positional/optional
    parser.add_argument("num1", help="Number 1", type=float)    # positional parameters
    parser.add_argument("num2", help="Number 2", type=float)
    parser.add_argument("-o", "--operation", help="provide operator", default="+") # optional parameters (--)
    #parser.add_argument("-o", "--operation", help="provide operator", default="+") # optional parameters (--) and shorthand parameter also provided(-) single hyphen

    # Parse the arguments
    args = parser.parse_args()
    print(args)
    if args.operation == "+":
        print(args.num1 + args.num2)
    if args.operation == "-":
        print(args.num1 - args.num2)

# client code
python test.py 80 20 --operation +    # With optional args
python test.py 80 20 -o +             # shorthand notation with single hyphen
python test.py 80 20 -o=+             # = and space are allowed 
```

# Lambda, Filter, Map, Reduce
- lambda : these are anonymous functions
- lambda functions falls into functional programming paradigm
- these are also known as 1 line function
- lambda functions are generally used with the functions, which takes functions as an argument or return functions as a result
- functions are 1st class citizen in functional programming
- we can use lambda functions with functions like `filter map reduce`
```python
double = lambda x : x * 2
add = lambda x, y : x + y
product = lambda x, y, z : x*y*z

#client code
print(add(3,5))
print(double(3))
```

# map function
- map will apply lambda function to each and every element of the list
```python
my_list = [1,2,3,4,5]

# map syntax : map(function, iterable)    -> returns a map object -> typecast it into a list to see the result
ans = map(lambda x : x * 2, my_list)
print(list(ans))
```

### Add two lists using the map and lambda function
```python
my_list = [1,2,3,4,5]
my_list2 = [6,7,8,9,10]

ans = map(lambda x, y : x + y, my_list, my_list2)
print(list(ans))
```
# filter function
- It takes 2 args, function as 1st argument(a function which gives us a boolean result)

### Find even values from a list using filter function
```python
my_list = [1,2,3,4,5]
c = filter(lambda x: x%2 == 0, my_list)
print(list(c))
```

### Find values greater than 5 in a list
```python
my_list = [4,8,1,3,7]
c = filter(lambda x: True if x > 5 else False, my_list)    # both if and else are mandatory
print(list(c))
```

# reduce function
- we need to import `functools` module to use reduce function
- It also takes 2 args, 1st function and 2nd is the iterable collection
- The below function is finding out sum of the entire list
- It takes first 2 elements as x and y and apply operation. Then the result is passed as x, for next operation and other value is taken as y for the collection.
- Repeating the above computation on the entire sequence, it returns the sum of the list as the final answer.
```python
from functools import reduce
my_list = [4,8,1,3,7]
e = reduce(lambda x, y : x + y, my_list)
print(e)
```

# Python closures and nested functions
```python
# outer function is also called enclosing function
# inner function is also called local function
def outer_func(text):
    def inner_func():   # this fn is declared locally inside the outer function
        print(text)
    inner_func()        # We are just calling the inner function inside the outer function  

#client code
outer_func("hello")
```
# closure
- In order to convert nested function into a closure, we need to return the inner function and remove the () from the inner function return statement
- closure is a function, whose return value depends on 1 or more variables which are declared outside the function
- closure function object remembers the value, in the enclosing scope even if they are not present in the memory.
- it is able to remember the values, which are declared outside the function also.
- It is heavily used in decorators in python

```python
def outer_func(text):
    def inner_func():   
        print(text)
    return inner_func   # converted into a closure  

#client code
a = outer_func("hello")
del outer_func            # delete outer function
print(a())                # now, also it will work
```

```python
def nth_power(exponent):
    def pow_of(base):
        return pow(base, exponent)
    return pow_of

square = nth_power(2)
cube = nth_power(3)


print(square(16))    # prints 256
print(cube(3))       # prints 27
```

# Decorators
- Decorators wraps a function and modify its behavior, without changing the code of the function
```python
def decorator_func(func):
    def wrapper():
        print("********************")
        func()
        print("********************")
    return wrapper

def say_hello():
    print("hello_world")

# 1st way
hello = decorator_func(say_hello)
hello()

# 2nd way (declare it above the function)
# @decorator_func
# def say_hello():
#     print("hello_world")
```

## Using multiple decorator functions
- They are executed in the bottom to top order. First decorator_X will be executed, next decorator_Y
```python
def decorator_X(func):
    def wrapper():
        print("X"*20)
        func()
        print("X"*20)
    return wrapper

def decorator_Y(func):
    def wrapper():
        print("Y"*20)
        func()
        print("Y"*20)
    return wrapper

@decorator_Y
@decorator_X
def say_hello():
    print("hello_world")

# client code
say_hello()
```

## more examples
```python
# We decorated divide function, w/o changing its src code
def decorator_divide(func):
    def wrapper(x, y):
        print(f" x : {x}  y: {y}")
        if y == 0:
            print("division with zero not allowed")
                return
        return x / y
    return wrapper

def divide(x/y):
    return x / y
```

```python
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

# client code
a = list(range(2000000))
my_func(a)
```

# Operator overloading (Check in your project where you have done it)
```python
__add__
__sub__
```

# pdb (python Debugger)
```python
python -m pdb <script_name>
python -m pdb test.py
# type help in pdb to get the list of all commands that can be used
```
Three most frequently used commands are:
- n Or next command
- s Or step command
- c Or continue command
- h Or help command
- w Or where command (tells where currently pdb is)
- You can also type ```help <command_name>``` to read more about a particular command
- Once your program is finished, pdb will restart it from beginning
- whatis command :- Tells the type of a variable
- break :- Helps to set breakpoint Ex. break 9 (set breakpoint at line 9)

## Using pdb in code
```python
import pdb
def add(x,y):
    sum = x + y
    return sum

x = input("Number 1:")
y = input("Number 2:")
pdb.set_trace()        # Runs code and at this point set the program in pdb terminal mode
z = add(x,y)
print(z)

# client code
python test.py # no need to pass -m pdb now
```

# How to use Pycharm to debug python code
- It is a good IDE for python development. Definitely worth learning, if we need to work in python

# Pip and PyPi for managing python packages
- pip is a commandline tool for installing and managing python packages which are generally found on a special index called as PyPI
- pypi is a repository of softwares for python programming language
- `pip search <pkg_name>` to seach for the package
- `pip list` to check the list of all installed packages

# install packages using pycharm
-  Goto File -> settings -> Select Your project -> Select Project interpreter -> Click on + -> search your package -> install it.

# Global, local and Nonlocal Variables in python
- local variables have more priority over global variables
```python
def func():
    print(x)      # This line will throw ERROR, as python is confused here, whether x is local variable or global variable
    x = "local"
    print(x)

x = "global"
func()
print(x)
```

## non-local variables
- non-local variables behave similar to global variables, but they have some differences.
- These variables are mostly used inside the nested functions.
- not used that much
