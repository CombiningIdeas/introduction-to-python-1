'''
Задание 3
Подсчитать количество целых чисел в диапазоне
от 100 до 9999 у которых все цифры разные.
'''

class numeral:

    def integer():
        result11 = 0
        leftBorder11 = 1000
        rightBorder11 = 9999

        for index11 in range(leftBorder11, rightBorder11 + 1):

            variableOne11, variableTen11, variableHundred11, variableThousand11 = str(index11)

            if variableOne11 != variableTen11 and variableOne11 != variableHundred11 and variableTen11 != variableHundred11 and \
               variableThousand11 != variableOne11 and variableTen11 != variableThousand11 and variableHundred11 != variableThousand11:
                result11 += 1
        
        result22 = 0
        leftBorder22 = 100
        rightBorder22 = 999

        for index22 in range(leftBorder22, rightBorder22 + 1):

            variableOne22, variableTen22, variableHundred22 = str(index22)

            if variableOne22 != variableTen22 and variableOne22 != variableHundred22 and variableTen22 != variableHundred22:
                result22 += 1

        result33 = result11 + result22

        print("количество целых чисел в диапазоне от 100 до 9999 у которых все цифры разные:",result33)
        
numeral.integer()

#Второй способ решения

result4 = 0
leftBorder4 = 100
rightBorder4 = 999

for index4 in range(leftBorder4, rightBorder4 + 1):
    decomposition = str(index4)
    if decomposition[0] != decomposition[1] and decomposition[0] != decomposition[2] and decomposition[1] != decomposition[2]:
        result4 += 1


result5 = 0
leftBorder5 = 1000
rightBorder5 = 9999

for index5 in range(leftBorder5, rightBorder5 + 1):
    decomposition = str(index5)
    if decomposition[0] != decomposition[1] and decomposition[0] != decomposition[2] and decomposition[1] != decomposition[2] and \
       decomposition[0] != decomposition[3] and decomposition[1] != decomposition[3] and decomposition[2] != decomposition[3]:
        result5 += 1

result6 = result4 + result5

print("количество целых чисел в диапазоне от 100 до 9999 у которых все цифры разные:",result6)
