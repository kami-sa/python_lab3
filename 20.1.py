SYMBOLS = {'.', ',', ':', ';', '-'}
VOWELS = {'а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'ё', 'А', 'Е', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я', 'Ё'}


def translate(string):
    new_string = ''
    for i in range(len(string)):
        if string[i] not in SYMBOLS and string[i] not in VOWELS:
            new_string += string[i]
    return new_string


translatedText = None
translatedText = translate("Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто читать. "
                           "Достаточно небольшой тренировки - и вы сможете это делать.")
print(translatedText)
