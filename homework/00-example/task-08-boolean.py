year = 2024

is_standard = (year % 4 == 0) and (year % 100 != 0)
is_century = (year % 400 == 0)
is_leap = is_standard or is_century
print(is_leap)