is_on_time = input("Сдана в срок? (да/нет): ")
points = int(input("Количество баллов: "))

if points < 0 or points > 10:
    print("Некорректное количество баллов")
else:
    if is_on_time == "да":
        if points >= 9:
            print("Отлично")
        elif points >= 7:
            print("Хорошо")
        elif points >= 5:
            print("Удовлетворительно")
        else:
            print("Неудовлетворительно")
    else:
        if points >= 5:
            print("Удовлетворительно")
        else:
            print("Неудовлетворительно")