has_subscription = input("Есть подписка? (да/нет): ")
minutes = int(input("Длительность поездки, мин: "))

if has_subscription == "да":
    if minutes <= 30:
        print("Поездка входит в подписку")
    else:
        cost = (minutes - 30) * 5
        print(f"Стоимость поездки: {cost} руб.")
else:
    cost = 50 + (minutes * 8)
    print(f"Стоимость поездки: {cost} руб.")