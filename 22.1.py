SYMBOLS = {'.', ',', ':', ';', '-', '?', '!'}


def encrypt_caesar(msg, shift = 3):
    new_msg = ""
    for i in range(len(msg)):
        if msg[i] != ' ' and msg[i] not in SYMBOLS:
            new_msg += chr(ord(msg[i]) + shift)
        else:
            new_msg += msg[i]
    return new_msg


def decrypt_caesar(msg, shift = 3):
    new_msg = ""
    for i in range(len(msg)):
        if msg[i] != ' ' and msg[i] not in SYMBOLS:
            new_msg += chr(ord(msg[i]) - shift)
        else:
            new_msg += msg[i]
    return new_msg


msg = "Да здравствует салат Цезарь!"
shift = 5
encrypted = encrypt_caesar(msg)
decrypted = decrypt_caesar(encrypted)
print(encrypted)
print(decrypted)

