prices = [120, 80, 450, 45, 990, 300]
threshold = int(input())
count = 0
for price in prices:
    if price > threshold:
        count += 1
print(f"Дороже порога: {count}")