'''
Практическая. Задание 1
Есть некоторый текст. Реализуйте следующую функциональность:
■ Изменить текст таким образом, чтобы каждое предложение начиналось с большой буквы;
■ Посчитайте сколько раз цифры встречаются в тексте;
■ Посчитайте сколько раз знаки препинания встречаются в тексте;
■ Посчитайте количество восклицательных знаков в
тексте
'''
'''
text = input("Введите текст: ")

dstText = ""
firstLetter = True

'''

class text():
    
     def offersWorks(self):
        text = input("Введите текст: ")
        
        dstText = ""
        firstLetter = True
        
        dstText = ""
        firstLetter = True
        for ii in text:
            if firstLetter == True:

                if ii.isspace():
                    dstText += ii
                else:
                    dstText += ii.upper()
                    firstLetter = False
                    continue

            else:
                if ii in {".", "?", "!"}:
                    firstLetter = True

                dstText += ii

        print("Текст начинающийся с большой буквы:", dstText)

        counter = 0
        if ii.isdigit():
            counter += 1

            print(counter)
        print("Количесвто цифр в тексте:", counter)

        self.dash = text.count("-")
        quotation_marks = text.count("'")
        self.colon = text.count(";")
        self.semicolon = text.count(":")
        self.comma = text.count(",")
        self.point = text.count(".")
        self.exclamation = text.count("!")
        self.question = text.count("?")
        self.ellipsis = text.count("...")

        self.offers = self.dash + quotation_marks + self.colon + self.semicolon + self.semicolon + self.comma + self.point + self.exclamation + self.question + self.ellipsis

        print("знаков препинаний в тексте:", self.offers)
        print("Восклицательных знаков в тексте:", self.exclamation)

        
analysisText = text()
analysisText.offersWorks()


'''
text = input("Введите текст: ")

dstText = ""
firstLetter = True

for ii in text:
    if firstLetter == True:
        if ii.isspace():
            dstText += ii
        else:
            dstText += ii.upper()
            firstLetter = False
            continue

    else:
        if ii in {".", "?", "!"}:
            firstLetter = True

        dstText += ii




print("Текст начинающийся с большой буквы:", dstText)
'''
