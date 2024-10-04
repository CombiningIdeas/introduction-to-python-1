'''
Модуль 1. Введение в Python
Часть 2
Задание 1
Выведите на экран надпись Nothing will work unless
you do на разных строках. Пример вывода:
Nothing
will work
unless you do.
'''
#print("Nothing\nwill work\nunless you do.")


"""
Задание 2
Выведите на экран надпись " Anyone who stops learning
is old, whether at twenty or eighty" Henry Ford на разных
строках. Пример вывода:
“Anyone who
stops
learning is old,
whether at twenty or eighty”.
Henry Ford
"""
#print('"Anyone who\n\tstops\n\t\tlearning is old,\n\t\t\twhether\
#at twenty or eighty".\n\t\t\t\tHenry Ford')

"""
Задание 3
Пользователь вводит с клавиатуры два числа. Необ-
ходимо найти сумму чисел, разницу чисел, произведение
числе. Результат вычислений вывести на экран.

number1 = float(input("Введите число №1: "))
number2 = float(input("Введите число №2: "))
print(number1, '+', number2, '=', number1 + number2)
print(number1, '-', number2, '=', number1 - number2)
print(number1, '*', number2, '=', number1 * number2)
print(number1, '/', number2, '=', number1 / number2)
print(number1, '^', number2, '=', number1 ** number2)
print(number1, '//', number2, '=', number1 // number2)
print(number1, '%', number2, '=', number1 % number2)
"""

"""
Задание 4
Пользователь вводит с клавиатуры два числа. Первое
число — это значение, второе число процент, который
необходимо посчитать. Например, мы ввели с клавиатуры
50 и 10. Требуется вывести на экран 10 процентов от 50.
Результат: 5

value = float(input("Введите значение: "))
percent = float(input("Введите процент: "))
print(percent,'%', value, '=', value * percent / 100)
"""

"""
Задание 5
Напишите программу, вычисляющую площадь пря-
моугольника. Пользователь с клавиатуры вводит ширину
и высоту прямоугольника.

a = float(input("Ширину прямоугольника: "))
b = float(input("Высоту прямоугольника: "))
print('S =', a * b)
"""


"""
Модуль 1. Введение в Python.
Часть 3
Задание 1
Пользователь с клавиатуры вводит двухзначное чис-
ло. Например, 26. Нужно показать на разных строках
значение первого и второго разряда. В нашем случае это
будет выглядеть так:
2
6

number = int(input("Введите двухзначное число: "))
print(number // 10, '\n' + str(number % 10))
"""


'''
Задание 2
Пользователь с клавиатуры вводит трёхзначное число.
Например, 891. Нужно показать на разных строках зна-
чение первого, второго и третьего разряда. Также нужно
показать на отдельной строке сумму этих трёх чисел.
В нашем случае это будет выглядеть так:
8
9
1
18

number = int(input("Введите трёхзначное число: "))
digit0 = number % 10
number //= 10
digit1 = number % 10
digit2 = number // 10
print(digit2, '\n' + str(digit1), '\n' + str(digit0),
      '\n' + str(digit2 + digit1 + digit0))
'''

'''
Задание 3
Пользователь вводит с клавиатуры две цифры. Необ-
ходимо создать число, содержащее эти цифры. Например,
если с клавиатуры введено 9, 7, тогда нужно сформиро-
вать число 97.

digit1 = int(input("Введите цифру №1: "))
digit2 = int(input("Введите цифру №2: "))
print(10 * digit1 + digit2)
'''

'''
Задание 4
Пользователь вводит с клавиатуры температуру по
шкале Цельсия. Требуется перевести температуру в гра-
дусы по Фаренгейту и вывести на экран.

temperatureC = float(input("Введите температуру по шкале Цельсия: "))
print('температура в градусах по Фаренгейту: ', 9 * temperatureC / 5 + 32)
'''


'''
Модуль 2. Операторы ветвлений
Часть 1
Задание 1
Пользователь вводит с клавиатуры число. Необходи-
мо проверить его на четность и нечетность. Если число
четное требуется вывести на экран число и надпись Even
number. Если число нечетное выведите на экран число и
надпись Odd number.

number = int(input("Введите число: "))

if number % 2 == 0:
    print(number, 'Even number')
else:
    print(number, 'Odd number')
'''
   
'''
Задание 2
Пользователь вводит с клавиатуры число. Необхо-
димо проверить его на кратность 7. Если число кратно
требуется вывести на экран число и надпись Number is
multiple 7. Если число не кратно выведите на экран число
и надпись Number is not multiple 7.

number = int(input("Введите число: "))

if number % 7 == 0:
    print(number, 'Number is multiple 7')
else:
    print(number, 'Number is not multiple 7')
'''

'''
Задание 3
Пользователь вводит с клавиатуры два числа. Необ-
ходимо найти максимум из двух чисел и показать его на
экран.


number1 = float(input("Введите число №1: "))
number2 = float(input("Введите число №2: "))

if number1 > number2:
    print('max {', str(number1) + ';', number2, '} =', number1)
else:
    print('max {', str(number1) + ';', number2, '} =', number2)
'''

'''
Задание 5
Пользователь вводит с клавиатуры два числа. В зави-
симости от выбора пользователя нужно показать сумму
двух чисел, разницу двух чисел, среднеарифметическое
или произведение двух чисел.

import sys

number1 = float(input("Введите число №1: "))
number2 = float(input("Введите число №2: "))
print('1 - +, \n2 - -, \n3 - m, \n4 - *')
choice = int(input('Ваш выбор (1 - 4): '))

if choice < 1 or 4 < choice:
    print("Ошибка!")
    sys.exit()

match choice:
    case 1:
        print(number1, '+', number2, '=', number1 + number2)
    case 2:
        print(number1, '-', number2, '=', number1 - number2)
    case 3:
        print(number1, '+', number2, '=', (number1 + number2) / 2)
    case 4:
        print(number1, '*', number2, '=', number1 * number2)

import sys

chessCage1 = input("Введите координаты клетки №1: ")
chessCage2 = input("Введите координаты клетки №2: ")

if not chessCage1.isalnum() or not chessCage2.isalnum() or \
len(chessCage1) != 2 or len(chessCage2) != 2:
    print("Ошибка!")
    sys.exit()
    
chessCage1x = chessCage1[0]
chessCage1y = chessCage1[1]

chessCage2x = chessCage2[0]
chessCage2y = chessCage2[1]

if not chessCage1x.isalpha() or not chessCage2x.isalpha():
    print("Ошибка!")
    sys.exit()

chessCage1x = chessCage1x.lower()
chessCage2x = chessCage2x.lower()

if chessCage1x < 'a' or 'h' < chessCage1x or \
chessCage2x < 'a' or 'h' < chessCage2x:
    print("Ошибка!")
    sys.exit()

if not chessCage1y.isdecimal() or not chessCage2y.isdecimal():
    print("Ошибка!")
    sys.exit()

chessCage1y = int(chessCage1y)
chessCage2y = int(chessCage2y)

if chessCage1y < 1 or 8 < chessCage1y or \
chessCage2y < 1 or 8 < chessCage2y:
    print("Ошибка!")
    sys.exit()

chessCage1x = ord(chessCage1x) - ord('a') + 1
chessCage2x = ord(chessCage2x) - ord('a') + 1

if (chessCage1x + chessCage1y + chessCage2x + chessCage2y) % 2 == 0:
    print('цвет одинаковый')
else:
    print('цвет разный')
'''


'''
Модуль 2. Операторы ветвлений
Часть 2
Задание 1
Пользователь вводит с клавиатуры время в секун-
дах, прошедшее с начала дня. В зависимости от выбора
пользователя посчитать, сколько часов, минут и секунд
осталось до полуночи.

totalSeconds = int(input("Введите время в секундах, прошедшее с начала дня: "))
totalSeconds = 86400 - totalSeconds
seconds = totalSeconds % 60
minutes = totalSeconds // 60
hours = minutes // 60
minutes %= 60
print('осталось до полуночи:', hours, 'ч. :', minutes, 'м. :', seconds, 'с.')
'''

'''
Задание 2
Пользователь вводит с клавиатуры диаметр окруж-
ности. В зависимости от выбора пользователя посчитать
площадь или периметр окружности.

import sys, math

diametr = float(input("Введите диаметр окружности: "))
print('1) s, \n2) p, \n3) выход')
choice = int(input('Ваш выбор (1 - 3): '))

if choice < 1 or 3 < choice:
    print("Ошибка!")
    sys.exit()

match choice:
    case 1:
        print('s = ', math.pi * diametr ** 2 / 4)
    case 2:
        print('p = ', math.pi * diametr)
    case 3:
        sys.exit()
'''


'''
Задание 3
Пользователь вводит с клавиатуры стоимость одной
игровой приставки, их количество и процент скидки.
В зависимости от выбора пользователя посчитать общую
сумму заказа или стоимость одной приставки с учетом
скидки.


import sys

price = float(input("Введите стоимость одной игровой приставки: "))
number = int(input("Введите их количество: "))
discount = float(input("Введите процент скидки: "))

print('1) Общая сумма заказа, \
\n2) стоимость одной приставки с учетом скидки, \
\n3) выход')

choice = int(input('Ваш выбор (1 - 3): '))

if choice < 1 or 3 < choice:
    print("Ошибка!")
    sys.exit()

match choice:
    case 1:
        print('Общая сумма заказа: ', price * number * (1 -  discount / 100))
    case 2:
        print('стоимость одной приставки с учетом скидки: ', price * number * (1 -  discount / 100) / number)
    case 3:
        sys.exit()
'''


'''
Задание 4
Пользователь вводит с клавиатуры размер файла
в гигабайтах и скорость интернет-соединения в битах в се-
кунду. В зависимости от выбора пользователя посчитать,
за сколько часов или минут, или секунд скачается файл.

import sys

size = float(input("Введите размер файла в гигабайтах: "))
speed = int(input("Введите скорость интернет-соединения в битах в секунду: "))

print('1) за сколько часов скачается файл, \
\n2) за сколько минут скачается файл, \
\n3) за сколько секунд скачается файл, \
\n4) выход')

choice = int(input('Ваш выбор (1 - 4): '))

if choice < 1 or 4 < choice:
    print("Ошибка!")
    sys.exit()

match choice:
    case 1:
        print('файл скачается за ', size * 2 ** 30 * 8 / speed / 3600, 'часов')
    case 2:
        print('файл скачается за ', size * 2 ** 30 * 8 / speed / 60, 'минут')
    case 3:
        print('файл скачается за ', size * 2 ** 30 * 8 / speed, 'секунд')
    case 4:
        sys.exit()
'''


'''
Задание 5
Пользователь с клавиатуры вводит количество часов.
Если полученное значение находится в диапазоне от 0 до
6 нужно вывести надпись Good Night, если в диапазоне от
6 до 13 Good Morning, если в диапазоне от 13 до 17 Good
Day, если в диапазоне от 17 до 0 Good Evening. Верхняя
граница диапазона не включается. Например, число 6
относится к 6 до 13

hours = int(input("Введите количество часов: "))

if 0 <= hours < 6 :
    print('Good Night')
elif hours < 13 :
    print('Good Morning')
elif hours < 17 :
    print('Good Day')
else :
    print('Good Evening')
'''


'''
Модуль 2. Операторы ветвлений
Часть 3
Задание 1
Пользователь вводит с клавиатуры целое шестизнач-
ное число. Написать программу, которая определяет,
является ли введенное число — счастливым (Счастли-
вым считается шестизначное число, у которого сумма
первых 3 цифр равна сумме вторых трех цифр).
Например, 123321 — счастливое число, так как 1+2+3 =
3+2+1.
С другой стороны 378423 несчастливое число, так
как 3+7+8 != 4+2+3.
Если пользователь ввел не шестизначное число тре-
буется вывести сообщение об ошибке.

number = int(input("Введите целое шестизначное число: "))

low3Digits = number % 1000
high3Digits = ( number - low3Digits ) // 1000

lowSum = 0
highSum = 0

for ii in range(3) :
    lowSum += low3Digits % 10
    low3Digits //= 10

    highSum += high3Digits % 10
    high3Digits //= 10

if lowSum == highSum :
    print(number, 'является счастливым')
else :
    print(number, 'не является счастливым')
'''
'''
import sys

number = int(input("Введите целое шестизначное число: "))

if number < 0 or 999999 < number :
    print("Ошибка!")
    sys.exit()

numberCopy = number

digit0 = number % 10
number //= 10
digit1 = number % 10
number //= 10
digit2 = number % 10
number //= 10
digit3 = number % 10
number //= 10
digit4 = number % 10
number //= 10
digit5 = number

if digit0 + digit1 + digit2 == digit3 + digit4 + digit5 :
    print(numberCopy, 'является счастливым')
else :
    print(numberCopy, 'не является счастливым')
'''


'''
Задание 2
Пользователь вводит шестизначное число. Необходимо
поменять в этом числе первую и шестую цифры, а также
вторую и пятую цифры.
Например, 723895 должно превратиться в 593827.
Если пользователь ввел не шестизначное число тре-
буется вывести сообщение об ошибке.

import sys

number = int(input("Введите целое шестизначное число: "))

if number < 0 or 999999 < number :
    print("Ошибка!")
    sys.exit()

digit0 = number % 10
number //= 10
digit1 = number % 10
number //= 10
digit2 = number % 10
number //= 10
digit3 = number % 10
number //= 10
digit4 = number % 10
number //= 10
digit5 = number

temp = digit0
digit0 = digit5
digit5 = temp

temp = digit1
digit1 = digit4
digit4 = temp

print(digit0 + digit1 * 10 + digit2 * 100 + digit3 * 1000 + digit4 * 10000 + digit5 * 100000)
'''


'''
Задание 3
Пользователь вводит с клавиатуры номер месяца (от 1
до 12). В зависимости от полученного номера месяца про-
грамма выводит на экран надпись: Winter (если введено
значение 1,2 или 12), Spring (если введено значение от 3
до 5), Summer (если введено значение от 6 до 8), Autumn
(если введено значение от 9 до 11).
Если пользователь ввел значение не в диапазоне от 1
до 12 требуется вывести сообщение об ошибке.
'''

#import sys

#month = int(input("Введите номер месяца: "))

#if month < 1 or 12 < month :
#    print("Ошибка!")
#    sys.exit()

#if 3 <= month <= 5 :
#    print('Spring')

'''
Задание 1
Пользователь вводит с клавиатуры номер дня
недели (1-7). Необходимо вывести на экран на-
звания дня недели. Например, если 1, то на экра-
не надпись понедельник, 2 — вторник и т.д.
'''

'''
import sys

number = int(input('Введите номер дня недели (1-7): '))

if number < 1 or 7 < number :
    print('Error!')
    sys.exit(1)

if number == 1 :
    print('Понедельник')
elif number == 2 :
    print('Вторник')
elif number == 3 :
    print('Среда')
elif number == 4 :
    print('Четверг')
elif number == 5 :
    print('Пятница')
elif number == 6 :
    print('Суббота')
else :
    print('Воскресенье')
'''

'''
import sys

number = int(input('Введите номер дня недели (1-7): '))

if number < 1 or 7 < number :
    print('Error!')
    sys.exit(1)

match number :
    case 1 :
        print('Понедельник')

    case 2 :
        print('Вторник')

    case 3 :
        print('Среда')

    case 4 :
        print('Четверг')

    case 5 :
        print('Пятница')

    case 6 :
        print('Суббота')
    
    case 7:
        print('Воскресенье')
'''

'''
import sys

number = int(input('Введите номер дня недели (1-7): '))

if number < 1 or 7 < number :
    print('Error!')
    sys.exit(1)

weekDays = [ 'Понедельник',  'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота',
            'Воскресенье' ]

print(weekDays[number - 1])
'''

'''
import sys

number = input('Введите имя дня недели по английски: ')

weekDays = { 'Monday' : 'Понедельник', 'Tuesday' : 'Вторник', 3 : 'Wednesday',
            'Thursday': 'Четверг', 'Friday' : 'Пятница', 'Saturday' : 'Суббота',
            'Sunday' : 'Воскресенье' }

print(weekDays[number])
'''

'''
def mean(a, b):
    return (a + b)/2

print(mean(5, 7))
'''

#import os

#def setGreenColor():
#    print('\x1b[6;30;42m', end = '')

#def resetDefaultColor():
#    print('\x1b[0m', end = '')

#def printNSymbol(number, symbol):
#    string = ""

#    for ii in range(number):
#        string += symbol

#    print(string, end = '')
#    resetDefaultColor()

#def print_triangle(number, symbol):
#    for jj in range(number):
#        printNSymbol(39 - jj, " ")
#        setGreenColor()
#        print('/', end = '')
#        printNSymbol(jj * 2 + 1, symbol)
#        setGreenColor()
#        print('\\', end = '')
#        resetDefaultColor()
#        print()

#def trapezoid(length, symbol):
#     for jj in range(2, length - 1):
#        printNSymbol(39 - jj, " ")
#        setGreenColor()
#        print('/', end = '')
#        printNSymbol(jj * 2 + 1, symbol)
#        setGreenColor()
#        print('\\', end = '')
#        resetDefaultColor()
#        print()


#os.system('color')
#os.system('dir')

#symbol = "*"
#string = ""
#number = 7
#length = 5

#print_triangle(5, symbol)

#for ii in range(length):
#    trapezoid(8 + ii * 2, symbol)

#4! = 4 * 3!

'''
a = int(input("введите аргумент факториала "))
 
factorial = 1

while a > 1:
    factorial *= a
    a -= 1
    
print(factorial)
'''

'''
def factorial(n):
    if n == 0 :
        return 1

    return n * factorial(n-1)

n = int(input("введите натуральное число "))    
print(str(n) + '! =', factorial(n))
'''

'''
def fibonacci(n):
    if n >= 2:
        return fibonacci(n-1) + fibonacci(n-2)
    elif n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        print('Неправильный аргумент', n)

n = int(input('Введите n = '))
print(f'Число Фибоначи с № {n} =', fibonacci(n))
'''

'''
def adder(*arguments):
    sum = 0

    for ii in arguments:
        sum += ii

    return sum

def stringAdder(*arguments):
    sum = ''

    for ii in arguments:
        sum += ii

    return sum

print(adder(100, 200))
print(adder(100, 200, 551))
print(stringAdder('red', 'black'))
'''

'''
Задание 1
Показать таблицу умножения для числа, введенного
пользователем. Например, если пользователь вводит
число 7, нужно показать:
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
'''

'''
f = float(input('Введите число: '))

for ii in range(1, 11):
    print(f'{f} * {ii} = {f * ii}')
'''

'''
Задание 3
Пользователь вводит с клавиатуры две границы ди-
апазона и число. Если число не попадает в диапазон,
программа просит пользователя повторно ввести число,
и так до тех пор, пока он не введет число правильно. Про-
грамма отображает все числа диапазона, выделяя число
восклицательными знаками. Например:
1 2 3 !4! 5 6 7.
'''

'''
left = int(input('Введите левую границу диапазона: '))
right = int(input('Введите правую границу диапазона: '))
number = int(input('Введите число: '))

while left > number or number > right:
    print('Ошибка!')
    number = int(input('Введите число: '))

for ii in range(left, right + 1):
    if ii == number or ii == number + 1:
        print('!', end = '')

    print(ii, end = '')

if number == right:
    print('!', end = '')
'''

'''
Задание 4
Написать игру «Угадай число». Программа загадывает
число в диапазоне от 1 до 500. Пользователь пытается
его угадать. После каждой попытки программа выдает
подсказки, больше или меньше его число загаданно-
го. В конце программа выдает статистику: за сколько
попыток угадано число, сколько времени это заняло.
Предусмотреть выход по 0 в случае, если пользователю
надоело угадывать число.
'''

'''
import random, time, sys, math
b = int(input('Введите правую границу: '))
secretNumber = random.randint(1, b)
nAttempt = math.ceil(math.log2(b))
attemptNo = 1
startTime = time.time()
print(f'Угадайте число за {nAttempt} попыток')
print('Попытка №', attemptNo)
userNumber = int(input('Введите число: '))

while nAttempt > 1 and userNumber != secretNumber:

    attemptNo += 1
    print('Попытка №', attemptNo)
    nAttempt -= 1

    if userNumber == 0:
        print('Bye')
        sys.exit(0)
    elif userNumber < secretNumber:
        print(f'{userNumber} < загаданого числа')
    else:
        print(f'{userNumber} > загаданого числа')

    userNumber = int(input('Введите число: '))

print('Число попыток:', attemptNo)
print('Затраченное:', time.time() - startTime, 'c.')

if userNumber == secretNumber:
    print('Вы угадали')
elif userNumber != secretNumber:
    print('Компьютер загадал', secretNumber)
'''


'''
Пользователь вводит с клавиатуры два числа.
Нужно посчитать отдельно сумму четных, нечет-
ных и чисел, кратных 9 в указанном диапазоне, а
также среднеарифметическое каждой группы.
'''

'''
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
'''

'''
Пользователь вводит с клавиатуры два числа
(начало и конец диапазона). Требуется проана-
лизировать все числа в этом диапазоне. Нужно
вывести на экран:
1. Все числа диапазона;
2. Все числа диапазона в убывающем порядке;
3. Все числа, кратные 7;
4. Количество чисел, кратных 5.
'''

'''
a = int(input("Первое число: "))
b = int(input("Второе число: "))

print("Все числа диапозона:")

for ii in range(a, b+1):
    print(ii, ' ', end = '')

print("\nВсе числа диапозона в убывающем порядке:")

for ii in range(b, a - 1, -1):
    print(ii, ' ', end = '')

print("\nВсе числа кратные 7:")

counter5 = 0

for ii in range(a, b+1):
   if ii % 7 == 0:
       print(ii, ' ', end = '')

   if ii % 5 == 0:
       counter5 += 1

print("\nКоличество чисел, кратных 5:", counter5)
'''

'''
import sys

def powerNutural0(a, n):
    if n > 1:
        return a * powerNutural0(a, n - 1)
    elif n == 1:
        return a
    else:
        if a != 0:
            return 1
        else:
            print('0 ** 0 не определено!')
            sys.exit(-1)

def power(base, degree):
    if degree >= 0:
        powerNutural0(base, degree)
    else:
        if base != 0:
            return 1 / powerNutural0(base, -degree)
        else:
            print('Делениена 0 не определено!')
            sys.exit(-1)

base = float(input('Введите основание: '))
degree = int(input('Введите показатель: '))

print(base, '**', degree, '=', power(base, degree))
'''

'''
Подсчитать количество целых чисел в диапазо-
не от 100 до 999 у которых есть две одинаковые
цифры.
'''
'''
numberCounter = 0

for ii in range(100, 999 + 1):
    digit2 = ii // 100
    digit1 = ii // 10 % 10
    digit0 = ii % 10

    if digit0 == digit1 or digit1 == digit2 or digit0 == digit2:
        numberCounter += 1

print('quantity:', numberCounter)
'''

'''
Подсчитать количество целых чисел в диапазоне
от 100 до 9999 у которых все цифры разные.
'''
'''
counter = 0

for ii in range(100, 999 + 1):
    digit2 = ii // 100
    digit1 = ii // 10 % 10
    digit0 = ii % 10
    if digit2  != digit1 and digit1 != digit0 and digit0 != digit2:
        counter += 1
 
for ii in range(1000, 9999 + 1):
    digit2 = ii // 100 % 10
    digit1 = ii // 10 % 10
    digit0 = ii % 10
    digit3 = ii // 1000
    
    if digit2  != digit1 and digit1 != digit0 and digit0 != digit2 and digit3 != digit1 and digit3 != digit0 and digit3 != digit2:
        counter += 1

print(counter)
'''

'''
Курс: «Введение  в язык программирования Python Модуль 3.
Строки. Списки. Часть 1 Задание 1
Пользователь вводит с клавиатуры строку. Произве-
дите поворот строк и полученный результат выведите
на экран.
'''

'''
string = input('Введите строку: ')
print(string[::-1])
'''

'''
Задание 2
Пользователь вводит с клавиатуры строку. Посчи-
тайте количество букв, цифр в строке. Выведите оба
количества на экран.
'''
'''
string = input('Введите строку: ')
print('букв: ', len([ii for ii in string if ii.isalpha()]))
print('цифр: ', len([ii for ii in string if ii.isdigit()]))
'''

'''
Задание 3
Пользователь вводит с клавиатуры строку и символ
для поиска. Посчитайте сколько раз в строке встречается
искомый символ. Полученное число выведите на экран.
'''
'''
string = input('Введите строку: ')
symbol = input('Введите символ для поиска: ')
print(f'в строке "{string}" встречается символ "{symbol}":', string.count(symbol))
'''

'''
Модуль 4. Строки. Списки.
Часть 2
Задание 1
Есть некоторый текст. Реализуйте следующую функциональность:
■ Изменить текст таким образом, чтобы каждое пред-
ложение начиналось с большой буквы;
■ Посчитайте сколько раз цифры встречаются в тексте;
■ Посчитайте сколько раз знаки препинания встреча-
ются в тексте;
■ Посчитайте количество восклицательных знаков в
тексте.
'''
def isPunct(symbol):
    if symbol in '.,?!;:"-\'':
        return True
    else:
        return False

inText = input('Введите текст:\n\n')

outText = ''
firstLetter = True
nDigit = 0
nPunct = 0

for ii in inText:
    if firstLetter == True:
        if ii.isspace():
            outText += ii
        else:
            if ii not in {'.', '"', "'"}:
                outText += ii.upper()
                firstLetter = False
            else:
                outText += ii
    else:
        if ii in {'.', '?', '!'}:
            firstLetter = True

        outText += ii

    if ii.isdigit():
        nDigit += 1

#for ii in {'.', ',', '?', '!', ';', ':', '"', '-', "'", '...'}:
#    if inText.count(ii):
#        nPunct += 1

    if isPunct(ii):
        nPunct += 1

print('\n\nТекст с предложениями начинающимися с большой буквы:\n\n', outText, sep = '')
print('цифры встречаются в тексте: ', nDigit)
print('знаки препинания встречаются в тексте: ', nPunct)
print('количество восклицательных знаков в тексте: ', inText.count('!'))
