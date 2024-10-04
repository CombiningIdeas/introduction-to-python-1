'''
Задание 3
Пользователь вводит с клавиатуры число. Если число больше нуля нужно вывести надпись
«Number is positive», если меньше нуля «Number
is negative», если равно нулю «Number is equal
to zero»
'''

digit = float(input("Введите число: "))

if digit > 0:
    print("Number is positive")
elif digit < 0:
    print("Number is negative")
else:
    print("Number is equal to zero")
