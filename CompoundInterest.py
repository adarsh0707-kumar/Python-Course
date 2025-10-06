principle = 0
rate = 0
time = 0


while True:
  principle = float(input("Enter the principle amount: "))
  if principle < 0:
    print("Principle amount must be greater than 0.")
  else:
    break



while True:
  rate = float(input("Enter the rate of interest (as a percentage): "))
  if rate < 0:
    print("Rate of interest must be greater than 0.")
  else:
    break


while True:
  time = int(input("Enter the time (in years): "))
  if time < 0:
    print("Time must be greater than 0.")
  else:
    break


print(f"Principle: ${principle:.2f}")
print(f"Rate: {rate:.2f}%")
print(f"Time: {time} years")

total = principle * pow((1 + rate / 100), time)

print(f"Balance after {time} year(s): ${total:.2f}")