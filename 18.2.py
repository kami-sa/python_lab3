def ask_password(str):
    if str == 'password':
        print('Доступ разрешен')
        return True
    else:
        print('В доступе отказано')
        return False


flag = False
count = 0;
while flag is not True and count < 3:
    password = input('Введите пароль: ')
    flag = ask_password(password)
    count += 1
