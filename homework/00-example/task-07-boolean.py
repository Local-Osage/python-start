bottles = 48

shippable = (bottles % 6 == 0) and (bottles % 4 == 0)
print(shippable)