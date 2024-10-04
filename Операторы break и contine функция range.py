# Операторы break и contine. Функция range.

#break - досрочно прерывает цикл. Continue - прерывает текущую итерацию и осуществляет переход на следующую.

for n in range(1, 20):
    if n == 5:
        continue
    if n == 12:
        break
    print(n)

# Функция range - позволяет сгенерировать последовательность нужной длинны.

for x in range (1, 30):
    print(x, end = ". ")

# Формат функции range:
# range([начало], [конец], [шаг])
# Параметр шаг задает инкримент. По умолчанию это 1.

for kk in range(30, 1 - 1, -1):
    print(kk, end = " ")

# Есть механизм поддерживающий итерацию.

rng = range(1, 30)
rng.index(5)
rng.count(1)

# Еще примеры по использованию range

for i in range(10):
    print(i, end = " ")
print()


for jj in range(0, 50, 5):
    print(jj, end = " ")
