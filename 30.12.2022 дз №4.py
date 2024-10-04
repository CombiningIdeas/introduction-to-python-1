'''
Задание 4
Зарплата менеджера составляет 200$ + процент
от продаж, продажи до 500$ — 3%, от 500 до 1000
— 5%, свыше 1000 — 8%. Пользователь вводит с
клавиатуры уровень продаж для трех менеджеров. Определить их зарплату, определить лучшего менеджера, начислить ему премию 200$,
вывести итоги на экран.
'''

salary1 = float(input("Введите уровень продаж для первого менеджера: "))
salary2 = float(input("Введите уровень продаж для второго менеджера: "))
salary3 = float(input("Введите уровень продаж для третьего менеджера: "))


if salary1 <= 500:
    salary11 = (salary1 * 3)/100
    print(200 + salary11)
elif 500 < salary1 <= 1000:
    salary11 = (salary1 * 5)/100
    print(200 + salary11)
elif salary1 > 1000:
    salary11 = (salary1 * 8)/100
    print(200 + salary11)


if salary2 <= 500:
    salary22 = (salary2 * 3)/100
    print(200 + salary22)
elif 500 < salary2 <= 1000:
    salary22 = (salary2 * 5)/100
    print(200 + salary22)
elif salary2 > 1000:
    salary22 = (salary2 * 5)/100
    print(200 + salary22)


if salary3 <= 500:
    salary33 = (salary3 * 3)/100
    print(200 + salary33)
elif 500 < salary3 <= 1000:
    salary33 = (salary3 * 5)/100
    print(200 + salary33)
elif salary3 > 1000:
    salary33 = (salary3 * 8)/100
    print(200 + salary33)



if salary1 <= salary2 and salary2 < salary3:
    print("Лучший менеджер получает премию 200 баксов:", salary33 + 200 + 200)
elif salary2 <= salary1 and salary1 < salary3:
    print("Лучший менеджер получает премию 200 баксов:", salary33 + 200 + 200)
    

if salary1 <= salary3 and salary3 < salary2:
    print("Лучший менеджер получает премию 200 баксов:", salary22 + 200 + 200)
elif salary3 <= salary1 and salary1 < salary2:
    print("Лучший менеджер получает премию 200 баксов:", salary22 + 200 + 200)


if salary2 <= salary3 and salary3 < salary1:
    print("Лучший менеджер получает премию 200 баксов:", salary11 + 200 + 200)
elif salary3 <= salary2 and salary2 < salary1:
    print("Лучший менеджер получает премию 200 баксов:", salary11 + 200 + 200)
