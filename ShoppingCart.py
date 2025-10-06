# Exercise 2 shopping cart program

item = input("Enter the item you want to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many do you want to buy?: "))

total = price * quantity

print(f"You have bought {quantity} {item}(s) for a total of ${total:.2f}")