'''
Задание 3
Показать на экран таблицу умножения в диапазоне, указанном пользователем. Например, если
пользователь указал 3 и 5, таблица может выглядеть так:
3*1 = 3 3*2 = 6 3*3 = 9 ... 3 * 10 = 30
.............................................................................
5*1 = 5 5 *2 = 10 5 *3 = 15 ... 5 * 10 = 50
'''

#Таблица умножения в указанном диапазоне:
left_board = int(input("Введите левую границу диапазона: "))
right_board = int(input("Введите правую границу диапазона: "))

class multiplication_table:

    def action(self):
        number1, number2, number3, number4, number5, number6, number7, number8, number9, number10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for count in range(left_board, right_board + 1):
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
