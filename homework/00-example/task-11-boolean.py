cashier_1 = "нет"
cashier_2 = "да"
cashier_3 = "нет"

open_1 = cashier_1 == "да"
open_2 = cashier_2 == "да"
open_3 = cashier_3 == "да"

only_one = (open_1 + open_2 + open_3) == 1
print(only_one)