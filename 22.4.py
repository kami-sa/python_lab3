import math


def solve(*coefficients):
    x = []
    if len(coefficients) == 3:
        a = coefficients[0]
        b = coefficients[1]
        c = coefficients[2]
        d = (b ** 2) - 4 * a * c
        if d >= 0:
            x.append((-b + math.sqrt(d)) / (2 * a))
            x.append((-b - math.sqrt(d)) / (2 * a))
        else:
            x.append('Нет действительных решений')
    elif len(coefficients) == 2:
        b = coefficients[0]
        c = coefficients[1]
        x.append(-c / b)
    else:
        x.append(None)
    return x


# print(solve(2,1))
# print(solve(1, 2, 1))
# print(solve(2,-6,0))