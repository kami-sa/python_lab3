# a и b - строки, разделенные ";", после split a0 и b0 - координтаы точек по Ох, a1 и b1 - координтаы по Оу
def equation(a, b):
    a = a.split(';')
    b = b.split(';')
    for i in range(2):
        a[i] = float(a[i])
        b[i] = float(b[i])
    if (a[0] - b[0]) != 0:
        k = (a[1] - b[1]) / (a[0] - b[0])
        b = (a[0] * b[1] - b[0] * a[1]) / (a[0] - b[0])
    else:
        print(0.0)
        return
    if k != 0 and b != 0:
        print(k, ',', b)
    elif b == 0:
        print(k)
    elif k == 0:
        print(b)


string = input('Введите координаты двух точек, принадлежащих прямой. '
               'Для каждой точки координаты разделите ";", а точки разделите пробелом: ')
string = string.split()
equation(string[0], string[1])
