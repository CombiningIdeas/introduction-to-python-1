'''
def mean(a, b):
    return (a + b)/2

print(mean(5, 7))
'''

import os

def printNSymbol(number, symbol):
    string = ""

    for ii in range(number):
        string += symbol

    print(string, end = '')
    print('\x1b[0m', end = '')

def print_triangle(number, symbol):
    for jj in range(number):
        printNSymbol(39 - jj, " ")
        print('\x1b[6;30;42m', end = '')
        print('/', end = '')
        printNSymbol(jj * 2 + 1, symbol)
        print('\x1b[6;30;42m', end = '')
        print('\\', end = '')
        print('\x1b[0m', end = '')
        print()

def trapezoid(length, symbol):
     for jj in range(2, length - 1):
        printNSymbol(39 - jj, " ")
        print('\x1b[6;30;42m', end = '')
        print('/', end = '')
        printNSymbol(jj * 2 + 1, symbol)
        print('\x1b[6;30;42m', end = '')
        print('\\', end = '')
        print('\x1b[0m', end = '')
        print()


os.system('color')

symbol = "*"
string = ""
number = 7
length = 5

print_triangle(5, symbol)

for ii in range(length):
    trapezoid(8 + ii * 2, symbol)

