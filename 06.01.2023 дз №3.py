'''
Задание 3
Пользователь вводит с клавиатуры числа. Если число больше нуля нужно вывести надпись
«Number is positive», если меньше нуля «Number
is negative», если равно нулю «Number is equal to
zero». Когда пользователь вводит число 7 программа прекращает свою работу и выводит на
экран надпись «Good bye!»

'''

import sys

digit = float(input("Введите число: "))


while True:
    if digit == 7:
        print("Good bye!")
        sys.exit([0])
    
    if digit > 0:
        print("Number is positive")
        digit = float(input("Введите число: "))

    if digit < 0:
        print("Number is negative")
        digit = float(input("Введите число: "))

    if digit == -0:
        print("Number is equal to zero")
        digit = float(input("Введите число: "))

    

