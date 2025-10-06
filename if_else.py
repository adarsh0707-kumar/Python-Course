# if = Do something based on a condition
# else = Do something if the condition is not met
# elif = Else if, to check multiple conditions

age = int(input("Enter your age: "))

if age >= 18:
  print("You are an adult")
elif age < 0:
  print("You haven't been born yet")
else:
  print("You are a minor")