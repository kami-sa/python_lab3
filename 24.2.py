word_list = []
while True:
    word = input()
    if word == '':
        break
    word_list.append(word)
a = sorted(word_list, key=lambda x: sum([ord(i) - ord('A') + 1 for i in x.upper()]))
print(*a)