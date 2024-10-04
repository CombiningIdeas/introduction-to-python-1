'''
number = int(input("Введите трехзначное число: "))
digit0 = number % 10
number //= 10
digit1 = number % 10
digit2 = number // 10
print(digit2, '\n' + str(digit1), '\n' +str(digit0))
'''

'''
number = int(input("Введите двухзначное число: "))
print(number // 10, '\n' + str(number % 10))
'''

'''
number = int(input("Введите трехзначное число: "))
digit0 = number % 10
number //= 10
digit1 = number % 10
digit2 = number // 10
print(digit2, '\n' + str(digit1), '\n' +str(digit0),
      '\n' + str(digit2 + digit1 + digit0))
'''
