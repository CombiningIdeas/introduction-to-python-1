'''
Задание 2
Пользователь вводит с клавиатуры два числа
(начало и конец диапазона). Требуется проанализировать все числа в этом диапазоне. Нужно
вывести на экран:
1. Все числа диапазона;
2. Все числа диапазона в убывающем порядке;
3. Все числа, кратные 7;
4. Количество чисел, кратных 5.
'''

digit1 = int(input("Введите начало диапазона: "))
digit2 = int(input("Введите конец диапазона: "))


for array in range(digit1, digit2 + 1):
   print(array, end=' ')
print()


for array in range(digit2, digit1 - 1, -1):
   print(array, end=' ')
print()


for array in range(digit1, digit2 + 1):
    if array % 7 == 0:
       print(array, end=' ')
print()


for array in range(digit1, digit2 + 1):
   if array % 5 == 0:
       print(array, end=' ')
print()
