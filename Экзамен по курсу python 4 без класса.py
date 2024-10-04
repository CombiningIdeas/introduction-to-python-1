'''
Программа по работе с текстом.
Имеется текст, программа должна предоставить следующую
информация по этому тексту:
1) Количество предложений
2) Количество слов
3) Количество чисел (не цифр)
Для считывания из файла, можно воспользоваться следующим кодом:
file = open("text.txt", encoding='utf-8')
text = file.read().replace('\n', ' ')
Пример работы программ
'''

'''
Текст:
После числа 100 идёт число 101, а потом уже идёт число 102?
Так что число 101 в этом случае не будет являться числом 102.
Я знаю, что так не бывает, но тут так написано, а значит, что тут может быть
всё что угодно!
И при этом, не является фактом, что это "что-то" не является числом 104.
Но в вопросе не было цифры 101 и поэтому, я должен был это учесть. Я учёл.
Вопрос, конечно, дурацкий, но, вот так вот. В этом случае я бы написал так:
число 101 не является числом 102.
'''
    
file = open("text.txt", encoding='utf-8')
text = file.read().replace('\n', ' ')
        
point = text.count(".")
exclamation = text.count("!")
question = text.count("?")
ellipsis = text.count("...")
    
offers = point + exclamation + question + ellipsis
    
print("Предложений в тексте:", offers)

        
def is_word(count_word):
    try:
        count_word
        return True
    except:
        return False

jj = 0
for count_word in text.split():
    if is_word(count_word) == True:
        jj += 1

                                        
print("Слов в тексте:", jj)

        
        
def is_number(numbers):
    try:
        int(numbers)
        return True
    except:
        return False

text1 = text.replace(",", " ,")
text2 = text1.replace(".", " .")
text3 = text2.replace("!", " !")
text4 = text3.replace("?", " ?")

nn = 0
for numbers in text4.split():
    if is_number(numbers) == True:
        nn += 1

print("Чисел в тексте:", nn)

