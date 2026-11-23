password = input("Пароль: ")
length = len(password)

if length >= 12:
    print("Надёжный пароль")
elif length >= 8:
    print("Средний пароль")
elif length < 8:
    print("Слабый пароль")