'''
Задание 4
Пользователь вводит два числа. Определить,
равны ли эти числа, и, если нет, вывести их на
экран в порядке возрастания.
'''

digit1 = float(input("Введите число№1: "))
digit2 = float(input("Введите число№2: "))

if digit1 > digit2:
    print(digit1, digit2)
elif digit1 < digit2:
    print(digit2, digit1)
else:
    print("числа равны")
