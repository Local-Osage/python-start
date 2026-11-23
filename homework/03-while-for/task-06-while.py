total_sum = 0
count = 0
while True:
    grade = int(input())
    if grade == 0:
        break
    total_sum += grade
    count += 1

if count == 0:
    print("Нет оценок")
else:
    average = total_sum / count
    print(f"Средний балл: {average:.2f}")