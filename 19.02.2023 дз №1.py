'''
Задание 1
Пользователь вводит с клавиатуры арифметическое выражение. Например, 23+12.
Необходимо вывести на экран результат выражения. В нашем примере это 35. Арифметическое выражение может состоять только из трёх
частей: число, операция, число. Возможные операции: +, -,*,/
'''

expression = input()


if "+" in expression:
    digit1 = int(expression[0:expression.find("+")])
    digit2 = int(expression[expression.find("+")+1::])
    result = digit1 + digit2

elif "-" in expression:
    digit1 = int(expression[0:expression.find("-")])
    digit2 = int(expression[expression.find("-")+1::])
    result = digit1 - digit2

elif "*" in expression:
    digit1 = int(expression[0:expression.find("*")])
    digit2 = int(expression[expression.find("*")+1::])
    result = digit1 * digit2

elif "/" in expression:
    digit1 = int(expression[0:expression.find("/")])
    digit2 = int(expression[expression.find("/")+1::])
    result = digit1 / digit2

print(result)
