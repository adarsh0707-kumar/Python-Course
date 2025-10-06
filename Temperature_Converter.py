unit = input("Is this temperature in Celsius or Fahrenheit (C/F)?: ")

temperature = float(input("Enter the temperature: "))

if unit.upper() == "C":
  converted = (temperature * 9/5) + 32
  print(f"{temperature}°C is {converted:.2f}°F")
elif unit.upper() == "F":
  converted = (temperature - 32) * 5/9
  print(f"{temperature}°F is {converted:.2f}°C")
else:
  print("Invalid unit, please use C or F")
  
# Exercise 4 Temperature Converter