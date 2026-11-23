correct_pin = 4821
for _ in range(3):
    pin = int(input())
    if pin == correct_pin:
        print("Доступ разрешен")
        break
    else:
        print("Карта заблокирована")