n = int(input())
words = [input().lower().strip() for i in range(n)]
words_set = set(set(words[i]) for i in range(n))
for i in range(len(words_set)):
