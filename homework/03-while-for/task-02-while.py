total_steps = 0
while True:
    steps = int(input())
    if steps == 0:
        break
    total_steps += steps
print(f"Общее количество шагов: {total_steps}")