'''
Задание 3.
Программа для заполнения списка целыми числами в указанном
диапазоне.
Пользователь вводит два числа: левую и правую границу диапазона. В
результате должен выводиться список целых чисел, от левой до правой
границы диапазона, включая эти границы. Если левая граница больше правой,
то следует сделать убывающий список.
*Дополнительно. Реализуйте задание, создав собственную функцию
`listInRange`, которая принимает два целых числа и возвращает список.
Пример работы программы:

'''
'''

beginning_range = int(input("Введите левую границу диапазона: "))
end_range = int(input("Введите правую границу диапазона: "))


if beginning_range < end_range:
   roster = [beginning_range, end_range + 1]# тут можно и без плюс 1, тогда к списку после 22 строки добваить 1 с помощью index.append(end_range + 1)
   index = list(range(*roster))
   print(index)

        
elif beginning_range > end_range:
    roster = [end_range, beginning_range + 1]
    index = list(range(*roster))
    index.reverse()# Обратный список.
    print(index)
    
elif beginning_range == end_range:
    print([beginning_range])




'''
#Дополнительное задание

beginning = int(input("Введите левую границу диапазона: "))
end = int(input("Введите правую границу диапазона: "))
 
def listInRange(beginning_range2, end_range2):

    if beginning_range2 < end_range2:
        roster = [beginning_range2, end_range2 + 1]# тут можно и без плюс 1, тогда к списку после 22 строки добваить 1
        #с помощью index.append(end_range2 + 1)
        index = list(range(*roster))
        return print(index)

    elif beginning_range2 > end_range2:
        roster = [end_range2, beginning_range2 + 1]
        index = list(range(*roster))
        index.reverse()# Обратный список.
        return print(index)

    elif beginning_range2 == end_range2:
        return print([beginning_range2])

listInRange(beginning, end)
