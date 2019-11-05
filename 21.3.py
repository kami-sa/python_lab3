def swap(f, s):
    for i in range(len(f)):
        f[i], s[i] = s[i], f[i]
    return f, s


first = [1, 2, 3]
second = [4, 5, 6]
swap(first, second)
print(*first)
print(*second)