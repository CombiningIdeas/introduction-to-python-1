'''
Задание 4
Пользователь вводит с клавиатуры числа. Программа должна подсчитывать сумму, максимум и
минимум, введенных чисел. Когда пользователь
вводит число 7 программа прекращает свою работу и выводит на экран надпись «Good bye!»
'''

# Я в начале не понял как должна работать программа, а потом до меня дошло, что она должна все время рабоать, а в конце выключаться
# когда введут 7 и тогда и нужно выводить сумму, максимум и минимум. А закоментрированный код просто решил оставить.
'''
import sys

numbers = int(input("Введите количесвто чисел: "))

for numeral in range(1, numbers + 1):
    digit = float(input("Введите числа: "))

    if digit == 7:
        print("Good bye!")
        sys.exit([0])
    digit += digit


summ = numeral
print(digit)
'''

# Это уже правильный код

import sys

digit = int(input("Введите число: "))

summ = 0
summ = summ + digit
maxNumber = digit
minNumber = digit

if digit == 7:
    print("Good bye!")
    sys.exit()
    
while True:
    digit = int(input("Введите число: "))
    
    if digit == 7:
        print("Good bye!") 
        break

    elif digit > maxNumber:
        maxNumber = digit

    elif digit < minNumber:
        minNumber = digit

    summ = summ + digit
 
print("Сумма введенных чисел равна: ", summ)
print("Максиммальное из введенных чисел это: ", maxNumber)
print("Минимальное из введенных чисел это: ", minNumber)
