rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
  for y in range(columns):
    print(symbol, end=" ")
  print()