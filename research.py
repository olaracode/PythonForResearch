import numpy as np
import math

x = np.array([1,3,5])
y = np.array([1,5,9])

# Getting the mean item

print(x.mean())
print(y.mean())
print(x.shape, y.shape) # This will return the size of the array

print(math.pi)  # returns the value of pi
math.sqrt(10)  # With sqrt you can print or get the square root of any item


m = math.pi / 2  # You can compute further math calculations

am = math.sin(math.pi/2)  # This will return the SIN value

"""
Numpy also has also a Square root function
with the np sqrt function you can calculate the square root of various objects at the same time
You can check what type of object is any given variable with the type function

type(variable)

You can also see the methods available for any variable or obj type ypu can use the dir() function

dir(variable/objType)

Yo can use the help(method) function and pass it a method name parameter to get more information about such method

When using python to compute math operations python has unlimited power to compute LONG numbers
That means that despite the length of a calculation python will still be able to process and print the largest number you can imagine

INTEGER DIVISIONS are use when you want the outcome of a division to be a integer and not a float

1/5 ----> normal division
1//5 ----> Integer division
to return the value of the ultimate operation you can use a _ and print it or use it for another calculation


Using the math module you can use Factorial calculations
3! is a factorial which represents 3*2*1 or if it was 5! it will be 5*4*3*2*1

math.factorial(3)
math.factorial(5)

these will do the same

Comparisons:
==, !=, <=, >=, >, <, is, or, and, not

Writing and reading files

filename = "input.txt"
for line in open(filename):
    print(line)
<
line.rstrip() method eliminates the /n in a string when you are reading files
x = open("anyfile.txt", "w") ---> Used to create a writable object
x.write("Any sequence of strings that you want to write to the given file")
x.close ---> used to finish the file writing

"""
print("-----------------------------------------------------------------------")
print("Scope Rules")
"""
SCOPE RULES(LEGB)
L local
E enclosing function
G global
B built-in

NUMPY
"""

zero_vector = np.zeros(5)
print("Vectors", zero_vector)
zero_matrix = np.zeros((5, 3))
print("Matrix\n", zero_matrix)
x = np.array([1, 2, 3])
y = np.array([2, 4, 6])
print(y.shape)

linspace = np.linspace(0,100,33)  # linearly spaced array. You use the start value, the final value and the ammount of items you desire
print(linspace)

logarithmicly = np.logspace(1,2,10) # Logarithmily spaced array. You use the start value, the final value and the ammount of items you desire

print(logarithmicly)

m = np.random.random(10)  # numpy includes its own random function. in this case we are using ity to get 10 items inside a variable
print("m", m)

print(np.any(x > 0.9))  # checks if any item fulfils the  condition
print(np.all(x >= 0.1))  # checks if ALL items fulfil the condition
