age = 30
answer = "да"

has_experience = answer == "да"

fits = age >= 18 and age <= 65 and has_experience
print("Подходит:", fits)