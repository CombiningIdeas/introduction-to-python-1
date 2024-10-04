'''
Задание 2
В списке целых, заполненном случайными числами, определить минимальный и максимальный
элементы, посчитать количество отрицательных
элементов, посчитать количество положительных элементов, посчитать количество нулей. Результаты вывести на экран.
'''

import random, math

quantity = int(input("Введите количество случайных чисел != 0: "))
borders = int(input("Введите число != 0: "))
reverseBorders = -borders

if reverseBorders < borders:
    randList = [random.randint(reverseBorders, borders) for index in range(0, quantity)]
    print("Список: ", randList)
    print("Максимальный элемент: ", max(randList), "; Минимальный элемент: ", min(randList), sep = "")
    print("количество отрицательных чисел:", sum(index < 0 for index in randList))
    print("количество оложительных чисел:", sum(index > 0 for index in randList))
    print("количество нулей:", sum(index == 0 for index in randList))
    
   
if borders < reverseBorders:
    randList = [random.randint(borders, reverseBorders) for index in range(0, quantity)]
    print("Список: ", randList)
    print("Максимальный элемент: ", max(randList), "; Минимальный элемент: ", min(randList), sep = "")
    print("количество отрицательных чисел:", sum(index < 0 for index in randList))
    print("количество оложительных чисел:", sum(index > 0 for index in randList))
    print("количество нулей:", sum(index == 0 for index in randList))
