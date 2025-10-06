weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds (K/L): ")

if unit.upper() == "K":
  converted = weight * 2.20462
  print(f"You are {converted:.2f} Pounds")
elif unit.upper() == "L":
  converted = weight / 2.20462
  print(f"You are {converted:.2f} Kilograms")
else:
  print("Invalid unit, please use K or L")