a = set()


def print_only_new(string):
    if string not in a:
        print(string)
    a.add(string)
    # a.add(string)


print_only_new('Шутка номер 1')
print_only_new('Шутка номер 2')
print_only_new('Шутка номер 1')
print_only_new('Шутка номер 3')
print_only_new('Шутка номер 4')
print_only_new('Шутка номер 2')
# print()
# print(*a, sep='\n')