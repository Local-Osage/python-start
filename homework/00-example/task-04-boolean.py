paid = "да"
in_stock = "да"
adress = "да"

is_paid = paid == "да"
is_in_stock = in_stock == "да"
is_adress = adress == "да"

can_send = is_paid and is_in_stock and is_adress
print("Можно отправлять:", can_send)

call = is_paid and (not is_adress)
print("Позвонить покупателю:", call)