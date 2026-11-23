category = input("Категория товара: ")
amount = int(input("Количество товара, руб.: "))

cashback_percent = 0

if category == "азс":
    cashback_percent = 5
elif category == "аптека":
    cashback_percent = 3
elif category == "супермаркет":
    cashback_percent = 1

cashback = amount * cashback_percent / 100
print(f"Кешбэк: {cashback:.2f} руб.")