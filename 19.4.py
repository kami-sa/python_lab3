def palindrome(string):
    if string[:] == string[::-1]:
        return 'Палиндром'
    else:
        return 'Не палиндром'


a = input()
print(palindrome(a))
