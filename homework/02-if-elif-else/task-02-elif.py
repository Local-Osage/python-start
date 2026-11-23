length = int(input("Длина, см: "))
width = int(input("Ширина, см: "))
height = int(input("Высота, см: "))
weight = float(input("Вес, кг: "))

if length <= 55 and width <= 40 and height <= 20 and weight <= 10:
    print("Можно взять в салон")
else:
    print("Нельзя взять в салон")