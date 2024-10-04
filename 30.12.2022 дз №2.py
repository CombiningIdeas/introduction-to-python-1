'''
Задание 2
Написать программу, которая по выбору пользователя возводит введенное им число в степень
от нулевой до седьмой включительно.
'''
#первый способ
'''
digit = float(input("Введите число: "))
power1 = pow(digit, 0)
power2 = pow(digit, 1)
power3 = pow(digit, 2)
power4 = pow(digit, 3)
power5 = pow(digit, 4)
power6 = pow(digit, 5)
power7 = pow(digit, 6)
power8 = pow(digit, 7)

print(power1, power2, power3, power4, power5, power6, power7, power8)
'''

#второй спсоб
digit = float(input("Введите число: "))
power1 = digit ** 0
power2 = digit ** 1
power3 = digit ** 2
power4 = digit ** 3
power5 = digit ** 4
power6 = digit ** 5
power7 = digit ** 6
power8 = digit ** 7

print(power1, power2, power3, power4, power5, power6, power7, power8)
