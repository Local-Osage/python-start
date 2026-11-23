charge = int(input("Заряд батареи, %: "))

if charge <= 15:
    print("Критический уровень заряда")
elif charge <= 50:
    print("Низкий уровень заряда")
elif charge <= 99:
    print("Нормальный уровень заряда")
else:
    print("Батарея заряжена")