n = int(input())
words = [input().lower().strip() for i in range(n)]
sort_words = []
for word in words:
    sort_words.append(sorted(word))
set_w = set()
for i in range(len(words)):
    if words[i] not in set_w:
        print(words[i], end=' ')
        set_w.add(words[i])
        for j in range(i+1, len(words)):
            if sort_words[i] == sort_words[j]:
                print(words[j], end=' ')
                set_w.add(words[j])
        print()
