def even(x):
    if x % 2 == 0:
        return True
    else:
        return False

for i in range(1, 11):
    print(i, even(i))
# even - проверяет на правду или лож, i - проверят число, идут по порядку от 1 до 10.
