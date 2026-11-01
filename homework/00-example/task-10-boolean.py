attendants = 80
labs_comp = 8
debt = 0

check_attend = attendants >= 75
print("Посещаемость:", check_attend)

check_labs = labs_comp >= 8
print("Лабораторные:", check_labs)

check_debt = debt == 0
print("Нет долга:", check_debt)

allowed = check_attend and check_labs and check_debt
print("Допущен:", allowed)