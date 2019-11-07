RU_DICT = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август',
           9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
EN_DICT = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
           9: 'September', 10: 'October', 11: 'November', 12: 'December'}


def month(m, lang):
    if lang == 'ru':
        print(RU_DICT[m])
        return RU_DICT[m]
    elif lang == 'en':
        print(EN_DICT[m])
        return EN_DICT[m]
    else:
        print('К сожалению, я не знаю такого языка. Введите ru, если русский, en - английский.')


mon = int(input())
language = input('Введите ru или en: ')
month(mon, language)
