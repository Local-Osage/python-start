allowed_speed = int(input("Введите разрешённую скорость, км/ч: "))
actual_speed = int(input("Введите фактическую скорость, км/ч: "))

excess = actual_speed - allowed_speed

if excess <= 20:
    fine = 0
elif excess <= 40:
    fine = 750
elif excess <= 60:
    fine = 1500
elif excess <= 80:
    fine = 2500
else:
    fine = 5000

print(f"Штраф: {fine} руб.")