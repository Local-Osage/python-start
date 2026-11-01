score_1 = 55
score_2 = 40
score_3 = 90

passed_1 = score_1 >= 40
passed_2 = score_2 >= 40
passed_3 = score_3 >= 40

passed_amount = passed_1 + passed_2 + passed_3
print("Сдано экзаменов:", passed_amount)

all_passed = passed_1 and passed_2 and passed_3
print("Сессия закрыта:", all_passed)