months = int(input("Отработано месяцев: "))
days_requested = int(input("Дней отпуска: "))

if months < 6:
    print("Отпуск не положен")
else:
    available_days = (months * 28) // 12
    print(f"Доступно дней отпуска: {available_days}")

    if days_requested <= available_days:
        print("Отпуск предоставлен")
    else:
        print("Не хватает дней: {missing_days}")