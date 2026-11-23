day = int(input("Введите день недели (1-7): "))
hour = int(input("Введите час (0-23): "))

if day in range(1, 6) and hour in range(9, 18):
    print("Оператор на связи")
elif day == 6 and hour in range(10, 15):
    print("Оператор на связи")
else:
    print("Оставьте заявку, ответим в рабочее время")