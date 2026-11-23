secret_number = 37
attempts = 0

for attempt in range(1, attempts + 1):
    guess = int(input())
    if guess == secret_number:
        print(f"Угадано с попытки {attempt}.")
        break
    elif guess < secret_number:
        print("Загаданное число больше.")
    else:
        print("Загаданное число меньше.")
else:
    print("Попытки закончились.")