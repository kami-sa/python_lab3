def from_string_to_list(string, container):
    string = string[::-1]
    string = string.split()
    i = 0;
    while len(string) != 0:
        container.append(string.pop())
        i += 1
    return container


# a = [1, 2, 3]
# from_string_to_list("1 3 99 52", a)
# print(*a)
# a = [77, 'abc']
# from_string_to_list("", a)
# print(*a)

