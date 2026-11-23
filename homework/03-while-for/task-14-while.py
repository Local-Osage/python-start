n = int(input())
total = 0
minimum = None

for i in range(n):
    temp = int(input())
    total += temp
    if minimum is None or temp < minimum:
        minimum = temp

average = total / n
print(f"Минимум: {minimum}")
print(f"Среднее: {average:.2f}")