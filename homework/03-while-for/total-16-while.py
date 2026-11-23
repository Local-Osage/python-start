n = int(input())
sum_divisors = 0

if n == 1:
    print("Не совершенное число")
else:
    for i in range(1, n):
        if n % i == 0:
            sum_divisors += i

    if sum_divisors == n:
        print("Совершенное число")
    else:
        print("Не совершенное число")