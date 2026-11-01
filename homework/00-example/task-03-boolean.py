height = 130
age = 12
accompany = "нет"

has_adult = accompany == "да"
can_ride = (height >= 120) and ((age >= 10) or has_adult)

print("Можно на аттракцион:", can_ride)