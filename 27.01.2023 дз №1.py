'''
Задание 1
Показать на экран все простые числа в диапазоне, указанном пользователем. Число называется
простым, если оно делится без остатка только на
себя и на единицу. Например, три — это простое
число, а четыре нет.
'''

import sys
while True:
    print("Выход из программы: 919101090")
    leftBorder = int(input("Введите начало диапазона: "))
    rightBorder =  int(input("Введите конец диапазона: "))
    if leftBorder < rightBorder:
        number = leftBorder - 1
        for index in range(leftBorder, rightBorder + 1):
            number += 1
            if index == 2 or index == 3 or index == 5 or index == -2 or index == -3 or index == -5:
                print(index)
            elif index == 0:
                continue
            else:
                if (index % number == 0) and (index % number == 0) and not (index % 2 == 0) and not(index % 3 == 0):
                    print(index)
    elif leftBorder > rightBorder:
        number = leftBorder + 1
        for index in range(leftBorder, rightBorder -1, -1):
            number -= 1
            if index == 2 or index == 3 or index == 5 or index == -2 or index == -3 or index == -5:
                print(index)
            elif index == 0:
                continue
            else:
                if (index % number == 0) and (index % number == 0) and not (index % 2 == 0) and not(index % 3 == 0):
                    print(index)
    elif leftBorder == rightBorder:
        number = leftBorder
        if index == 2 or index == 3 or index == 5 or index == -2 or index == -3 or index == -5:
            print(index)
        elif index == 0:
            continue
        else:
            if (leftBorder % number == 0) and (leftBorder % number == 0) and not (leftBorder % 2 == 0) and not(leftBorder % 3 == 0):
                print(leftBorder)
    else:
        print("Ошибка!")
        sys.exit([0])

    if leftBorder == 919101090 or rightBorder == 919101090:
        break
