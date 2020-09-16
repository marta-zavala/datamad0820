"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""
import random
import string

def RandomStringGenerator(c):
    return "".join([random.choice(string.ascii_lowercase + string.digits) for letra in range(c)])

def BatchStringGenerator(n, a=8, b=12):
    c = random.choice(range(a, b))
    return [RandomStringGenerator(c) for palabra in range(n)]

a = input('Enter minimum string length: ')
b = input('Enter maximum string length: ')
n = input('How many random strings to generate? ')

try:
    print(BatchStringGenerator(int(n), int(a), int(b)))
except:
    print('Incorrect min and max string lengths. Try again.')