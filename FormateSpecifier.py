# format specifiers = {value:flags} format a value with given flags

price1 = 47282.12345678
price2 = -1234.56789
price3 = 123456789.123456789

print(f"Price1 is ${price1:+,.2f}")  # .2f means 2 decimal places
print(f"Price2 is ${price2:+,.2f}") # 10 means total width 10, 3 decimal places
print(f"Price3 is ${price3:+,.2f}") # , means include commas as thousand separators, 2 decimal places