def simple_number(num):
    for i in range(2,num):
        if int(num/i) == float(num/i):
            return 'Составное число'
    return 'Простое число'


n = int(input())
print(simple_number(n))