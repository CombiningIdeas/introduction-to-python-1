'''
Задание 1
Пользователь вводит с клавиатуры два числа.
Нужно посчитать отдельно сумму четных, нечетных и чисел, кратных 9 в указанном диапазоне, а
также среднеарифметическое каждой группы.
'''

# У сеня не работает только среднее арифмитическое каждой группы, а все остальное я сделал, можете потом на уроке обьяснить, что нужно исправть.

number_left = int(input("Введите левую границу диапазона: "))
number_right = int(input("Введите правую границу диапазона: "))

sumEven = 0
counterEven = 0
sumOdd = 0
counterOdd = 0
sum9 = 0
counter9 = 0

for ii in range(number_left, number_right + 1):
    if ii % 2 == 0:
        sumEven += ii
        counterEven += 1       
    else:
        sumOdd += ii
        counterOdd += 1          
        
    if ii % 9 == 0:
        sum9 += ii
        counter9 += 1          


print("Сумма четных:", sumEven)
print("m(четных) =", sumEven / counterEven)
print("Сумма нечетных:", sumOdd)
print("m(нечетных) =", sumOdd / counterOdd)
print("Сумма кратных 9:", sum9)
print("m(кратных 9) =", sum9 / counter9)
