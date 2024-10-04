'''
Задание 1
Напишите программу, которая запрашивает два
целых числа x и y, после чего вычисляет и выводит значение x в степени y.
'''

import sys

base = float(input("Введите основание: "))
degree = int(input("Введите показатель: "))


def power(x, y):
    if y >= 1:
        composition1 = 1
        for index1 in range(1, y + 1):
            composition1 *= x
        return composition1


    elif y == 0:
        if x == 0:
            print("Неопределенно")
            sys.exit([0])
        elif x > 0 or x < 0:
            return 1


    elif y <= -1:
        upheaval = 1 / x
        composition2 = 1
        for index2 in range(1, abs(y) + 1):
            composition2 *= upheaval
        return composition2

    else:
        print("Ошибка")
        sys.exit([0])

print(base, "в степени", degree, "=", power(base, degree))
