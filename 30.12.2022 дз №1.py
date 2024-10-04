'''
Задание 1
Пользователь вводит с клавиатуры число в диапазоне от 1 до 100. Если число кратно 3 (делится на 3
без остатка) нужно вывести слово Fizz. Если число
кратно 5 нужно вывести слово Buzz. Если число
кратно 3 и 5 нужно вывести Fizz Buzz. Если число
не кратно не 3 и 5 нужно вывести само число.

'''

import sys

digit = float(input("Введите число от 1 до 100: "))

if 0 < digit < 101:
    if digit % 3 == 0 and digit %  5 == 0:
        print("Fizz Buzz")
    elif digit %  3 == 0:
        print("Fizz")
    elif digit %  5 == 0:
        print("Buzz")
    elif not digit %  3 == 0 and not digit % 5 == 0:
            print("digit")
else:
    print("Ошибка!!!")
    sys.exit([1])
