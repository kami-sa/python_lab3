def print_shrug_smile():
    print('¯\_(ツ)_/¯')


def print_ktulhu_smile():
    print('{:€')


def print_happy_smile():
    print('(͡° ͜ʖ ͡°)')


name = input('Введите название смайлика без круглых скобок: ')
if name == 'print_shrug_smile':
    print_shrug_smile()
elif name == 'print_ktulhu_smile':
    print_ktulhu_smile()
elif name == 'print_happy_smile':
    print_happy_smile()