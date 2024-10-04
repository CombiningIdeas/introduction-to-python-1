'''
number1 = float(input("Введите число №1: "))
number2 = float(input("Введите число №2: "))

if number1 > number2:
    print('max (', str(number1) + ';', str(number2), ') =', number1)
else:
    print('max (', str(number1) + ';', str(number2), ') =', number2)
'''

ledt_Board = int(input("Введите число №1: "))
right_Board = int(input("Введите число №2: "))
counter = 0
for list in range(max(ledt_Board, right_Board)):
    counter += 1

print(counter)

# Или можно просто использовать сипсок или картеж
