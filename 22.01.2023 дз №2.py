'''
Задание 2
Подсчитать количество целых чисел в диапазоне от 100 до 999 у которых есть две одинаковые
цифры.
'''


class numeral:
    
    def integer():
        result = 0
        leftBorder = 100
        rightBorder = 999

        for index1 in range(leftBorder, rightBorder + 1):
            
            variableOne = index1 % 10
            variableTen = index1 // 10 % 10
            variableHundred = index1 // 100

            # Почему то не работает закоментированный способ
#            variableOne, variableTen, variableHundred = str(index1)

            if variableOne == variableTen or variableOne == variableHundred or variableTen == variableHundred:
                result += 1
                
        print("количество целых чисел в диапазоне от 100 до 999 у которых есть две одинаковые цифры:",result)
        
numeral.integer()


# Болеее простой вариант способ решения

leftBorder = 100
rightBorder = 999

result = 0

for index1 in range(leftBorder, rightBorder + 1):
    
    variableOne = index1 % 10
    variableTen = (index1 // 10) % 10
    variableHundred = index1 // 100
    
#Почему то, что написано выше не работает, не понятно.
#    variableOne, variableTen, variableHundred = str(index1)
#А этот способ нашел в интернете, как переприсвоить сразу в строковое значение, а затем я просто написал сравнение
#Непонятно почему то что выше  написано не работает, хотя по логике должно работать и то же самое в классе, который я написал
    if variableOne == variableTen or variableOne == variableHundred or  variableTen == variableHundred:
        result += 1

print("количество целых чисел в диапазоне от 100 до 999 у которых есть две одинаковые цифры:",result)
    

