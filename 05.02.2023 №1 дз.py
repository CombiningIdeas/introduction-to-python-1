'''
Задание
Вывести на экран фигуры, заполненные зведочками.
Диалог с пользователем реализовать при помощи меню.
'''

import sys

value = str(input("Выберите одну любую фигуру соответствующую одной из букв [а, б, в, г, д, е, ж, з, и, к]:  "))

if value == "а":
    n = 8
    m = n - 8
    for index1 in range(n, -1, -1):
        for jj in range(m, 0, -1):
            print(end = " ")
        m = m + 2
        for inside in range(0, index1):
                print("*", end = " ")

        print() 
    
elif value == "б":
    for index2 in range(0, 8):
        for inside in range(0, index2 + 1):
            print("*", end = " ")

        print()


elif value == "в":
    n = 8
    m = n - 8
    for index4 in range(n, -1, -1):
        for j in range(m, 0, -1):
            print(end = " ")
        m = m + 1
        for inside in range(0, index4):
                print("*", end = " ")

        print()


elif value == "г":
    n = 8
    m = (2 * n) - 2
    for index4 in range(0, n):
        for j in range(0, m):
            print(end = " ")
        m = m - 1
        for inside in range(0, index4 + 1):
                print("*", end = " ")

        print() 

elif value == "д":
    n = 4
    m = n - 4
    for index4 in range(n, -1, -1):
        for j in range(m, 0, -1):
            print(end = " ")
        m = m + 1
        for inside in range(0, index4):
                print("*", end = " ")

        print()       

    l = 4
    k = (2 * l) - 5
    for index4 in range(0, l):
        for j in range(0, k):
            print(end = " ")
        k = k - 1
        for inside in range(0, index4 + 1):
                print("*", end = " ")

        print() 

elif value == "е":
# Тут не получилось
    for index6 in range(n, 0, -2):
        print((n - index6) * ' ' + index6 * '*')

elif value == "ж":
    n = 4
    for index7i in range(0, n):
        for index71 in range(0, index7i + 1):
            print("*", end=' ')
        print(" ")

    for index7j in range(n + 1, 0, -1):
        for index72 in range(0, index7j - 1):
            print("*", end=' ')
        print(" ") 

elif value == "з":
# И тут не получилось
    for index8 in range(n, 0, -2):
        print((n - index8) * ' ' + index8 * '*')

elif value == "и":
    for index9 in range(8, 0, -1):
        for inside in range(0, index9):
            print("*", end = " ")

        print()

elif value == "к":
# Тут почти получилось сделать фигуру, но все равно не выходит
    '''
    n = 8
    m = n - 8
    for index10 in range(0, n):
        for j in range(0, m):
            print(end = " ")
        m = m - 10
        for inside in range(0, index10 + 1):
            print(m * " " + "*", end = " ")

        print()

    '''
    for index2 in range(0, 8):
        for inside in range(0, index2 + 1):
            print("*", end = " ")

        print()
else:
    print("Ошибка! Неправильно указана буква фигуры!")
    sys.exit([0])
