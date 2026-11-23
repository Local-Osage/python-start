max_pulse = None
while True:
    pulse = int(input())
    if pulse == 0:
        break
    if max_pulse is None or pulse > max_pulse:
        max_pulse = pulse

if max_pulse is None:
    print("Нет данных")
else:
    print(f"Максимальный пульс: {max_pulse}")