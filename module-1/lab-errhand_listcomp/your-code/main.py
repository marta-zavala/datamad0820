#Example: 

eggs = (1,3,8,3,2)

my_listComprehension = [1/egg for egg in eggs]

print(my_listComprehension)

#Insert here the module/library import statements 
import math
import random
import os
import sys


#1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# Remember to use list comprehensions and to print your results
print("\nEjercicio 1:")
square=[i**2 for i in range (1,21)]
print(square)

#2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# Remember to use list comprehensions and to print your results
print("\nEjercicio 2:")
power_of_two = [numero**2 for numero in  range(1,51)]
print(power_of_two)

#3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# You will probably need to install math library with pip and import it in this file.  
# Remember to use list comprehensions and to print your results
print("\nEjercicio 3:")
sqrt = [math.sqrt(i) for i in range(1,101)]
print(sqrt)



#4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# Remember to use list comprehensions and to print your results
print("\nEjercicio 4:")
my_list = [i for i in range(-10,1)]
print(my_list)


#5. Find the odd numbers from 1-100. Use odds as the name of the list. 
# Remember to use list comprehensions and to print your results
print("\nEjercicio 5:")
odds = [i for i in range (1,101) if i%2==1]
print(odds)



#6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.
# Remember to use list comprehensions and to print your results
print("\nEjercicio 6:")
divisible_by_seven = [i for i in range (1,1001) if i%7==0]
print(divisible_by_seven) 



#7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# Remember to use list comprehensions and to print your results
# You can use the following test string but feel free to modify at your convenience
print("\nEjercicio 7:")
teststring = 'Find all of the words in a string that are monosyllabic'
vowels = ['a','e','i','o','u','A','E','I','O','U']
non_vowels = ["" if i in vowels else i for i in teststring]
print(non_vowels)


#8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'. 
# Use capital_letters as the name of the list.  
# Remember to use list comprehensions and to print your results
print("\nEjercicio 8:")
sentence = 'The Quick Brown Fox Jumped Over The Lazy Dog'
capital_letters = [i for i in sentence if i.lower() != i]
print(capital_letters)



#9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.
# Remember to use list comprehensions and to print your results.
print("\nEjercicio 9:")
sentence1 = 'The quick brown fox jumped over the lazy dog'
consonants = ["" if i in vowels else i for i in sentence1]
print(consonants)


#10. Find the folders you have in your madrid-oct-2018 local repo. Use files as name of the list.  
# You will probably need to import os library and some of its modules. You will need to make some online research.
# Remember to use list comprehensions and to print your results.
print("\nEjercicio 10:")
files = [x for x in os.listdir('/Users/mac/Desktop/Ironhack/datamad0820')]
print(files)


#11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list. 
#You will probably need to import random module
# Remember to use list comprehensions and to print your results
print("\nEjercicio 11:")

random_lists = [[random.randint(0,101) for i in range (10)] for i in range (4)]
print(random_lists)


#12. Flatten the following list of lists. Use flatten_list as the name of the output.
# Remember to use list comprehensions and to print your results
print("\nEjercicio 12:")


list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
flatten_list = [e for sub in list_of_lists for e in sub]
print(flatten_list)



#13. Convert the numbers of the following nested list to floats. Use floats as the name of the list. 
# Remember to use list comprehensions and to print your results.
print("\nEjercicio 13:")

list_of_lists = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'],
['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'],
['100', '100', '100', '100']]
floats = [float(e) for sub in list_of_lists for e in sub]
print(floats)


#14. Handle the exception thrown by the code below by using try and except blocks. 
print("\nEjercicio 14:")
try:
    for i in ['a','b','c']:
        print (i**2)
except Exception as e:
    print(type(e))


#15. Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'
# Check in provided resources the type of error you may use. 
print("\nEjercicio 15:")


x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("b no puede ser 0")
finally:
    print("All done")



#16. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 
print("\nEjercicio 16:")

try:
    abc=[10,20,20]
    print(abc[3])
except:
    pass


#17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user. 
# Hint: take a look on python input function. 
# Check in provided resources the type of error you may use. 

print("\nEjercicio 17:")

print(ZeroDivisionError)
print(TypeError)



#18. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

print("\nEjercicio 18:")

try:
    f = open('testfile','r')
    f.write('Test write this')
except:
    pass



#19. Handle the exceptions that can be thrown by the code below using try and except blocks. 
#Hint: the file could not exist and the data could not be convertable to int

print("\nEjercicio 19:")
try:
    fp = open('myfile.txt')
    line = f.readline()
    i = int(s.strip())
except:
    pass





#20. The following function can only run on a Linux system. 
# The assert in this function will throw an exception if you call it on an operating system other than Linux. 
# Handle this exception using try and except blocks. 
# You will probably need to import sys 

print("\nEjercicio 20:")
def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')


'''
# Bonus Questions:

# You will need to make some research on dictionary comprehension to solve the following questions

#21.  Write a function that asks for an integer and prints the square of it. 
# Hint: we need to continually keep checking until we get an integer.
# Use a while loop with a try,except, else block to account for incorrect inputs.




# 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9). 
# Use results as the name of the list 




# 23. Define a customised exception to handle not accepted values. 
# You have the following user inputs and the Num_of_sections can not be less than 2.
# Hint: Create a class derived from the pre-defined Exception class in Python

Total_Marks = int(input("Enter Total Marks Scored: ")) 
Num_of_Sections = int(input("Enter Num of Sections: "))
'''
