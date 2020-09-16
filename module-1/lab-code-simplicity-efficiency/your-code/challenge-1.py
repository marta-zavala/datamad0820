"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

print('Welcome to this calculator!\nIt can add and subtract whole numbers from zero to five')
a = input('Please choose your first number (zero to five, in letters): ')
b = input('What do you want to do? plus or minus: ')
c = input('Please choose your second number (zero to five, in letters): ')

num = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5}
numsol = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10}
op = ['plus','minus']

def get_keys_with_value(dic, value):
    return [key for key, val in numsol.items() if val == value]
try:
    if b == 'plus':
        print(f'{a} {b} {c} equal {(get_keys_with_value(numsol,num[a]+num[c])[0])}')
    elif b== 'minus':
        sol=num[a]-num[c]
        if sol>=0:
            print(f'{a} {b} {c} equal {get_keys_with_value(numsol,sol)[0]}')
        else:
            print(f'{a} {b} {c} equal negative {get_keys_with_value(numsol,sol*(-1))[0]}')

except Exception as e:
    print("I am not able to answer this question. Check your input, they must be written in letters.")

print("Thanks for using this calculator, goodbye :)")
