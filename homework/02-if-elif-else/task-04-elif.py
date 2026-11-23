start = int(input("Начало интервала, ч: "))
end = int(input("Конец интервала, ч: "))
arrival = int(input("Курьер Приехал, ч: "))

if arrival < start:
    print("Курьер приехал раньше времени")
elif arrival > end:
    print("Курьер приехал позже времени")
else:
    print("Курьер приехал вовремя")