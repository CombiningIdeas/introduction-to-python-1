'''
Задание 2
Показать на экране таблицу умножения для всех
чисел от 1 до 10. Например:
1 * 1 = 1 1 * 2 = 2 ….. 1 * 10 = 10
.............................................................................
10 * 1 = 10 10 * 2 = 20 …. 10 * 10 = 10
'''

#Таблица умножения от 1 до 10:
class multiplication_table:

    def action(self):
        number1, number2, number3, number4, number5, number6, number7, number8, number9, number10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for count in range(1, 10 + 1, 1):
            print(count, '*', number1, '=', number1 * count, end = " ")
            print(count, '*', number2, '=', number2 * count, end = " ")
            print(count, '*', number3, '=', number3 * count, end = " ")
            print(count, '*', number4, '=', number4 * count, end = " ")
            print(count, '*', number5, '=', number5 * count, end = " ")
            print(count, '*', number6, '=', number6 * count, end = " ")
            print(count, '*', number7, '=', number7 * count, end = " ")
            print(count, '*', number8, '=', number8 * count, end = " ")
            print(count, '*', number9, '=', number9 * count, end = " ")
            print(count, '*', number10, '=', number10 * count)

task = multiplication_table()
task.action()

