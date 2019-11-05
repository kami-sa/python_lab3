def translate(string):
    symbols = {'.', ',', ':', ';','-'}
    vowels = {'а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'ё', 'А', 'Е', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я', 'Ё'}
    new_string = ''
    for i in range(len(string)):
        if string[i] not in symbols and string[i] not in vowels:
            new_string += string[i]
    return new_string


translatedText = None
translatedText = translate("Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто читать. "
                           "Достаточно небольшой тренировки - и вы сможете это делать.")
print(translatedText)
