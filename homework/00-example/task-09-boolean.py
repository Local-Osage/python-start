price_1 = 1500
price_2 = 300

expensive_1 = price_1 > 1000
expensive_2 = price_2 > 1000

coupon = expensive_1 != expensive_2

print(coupon)