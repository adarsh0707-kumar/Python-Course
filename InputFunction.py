# input = A function to take input from user
# By default input function takes input as string

name = input("What is your name?: ")
age = int(input("How old are you?: "))

age = age + 1
print(f"Hello {name}")
print("HAPPY BIRTHDAY")
print(f"You are {age} years old")