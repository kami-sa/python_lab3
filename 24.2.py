word_upper_list = []
word_list = []
word_code = []
while True:
    word = input()
    if word == '':
        break
    word_list.append(word)
    word = word.upper()
    code = [ord(word[i]) - ord('A') + 1 for i in range(len(word))]
    word_code.append(sum(code))
    # word_upper_list.append(word)
word_dict = dict(zip(word_code, word_list))
list_keys = list(word_dict.keys())
list_keys.sort()
for i in list_keys:
    print(word_dict[i])
# print(*word_dict)