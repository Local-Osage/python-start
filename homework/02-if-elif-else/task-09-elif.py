a = int(input("Сторона a: "))
b = int(input("Сторона b: "))
c = int(input("Сторона c: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Треугольник не существует")
else:
    if a == b == c:
        print("Треугольник равносторонний")
    elif a == b or a == c or b == c:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")