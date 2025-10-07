n = int(input("Enter number of rows: "))
"""
for x in range(n):
  for y in range(n):
    print("symbol", end=" ")
  print()

"""
"""

for x in range(n):
  for y in range(x+1):
    print("*", end=" ")
  print()

"""
"""

for x in range(n):
  for y in range(x, n):
    print("*", end=" ")
  print()

"""

"""
for x in range(n):
  for y in range(x+1):
    print('', end=" ")
  for x in range(x, n):
    print("*", end=" ")

  print()
"""
"""
for x in range(n):
  for y in range(x, n):
    print('', end=" ")
  for x in range(x +1):
    print("*", end=" ")

  print()

"""
"""
for x in range(n):
  for y in range(x,n):
    print(' ', end=" ")
  for y in range(x + 1):
    print("*", end=" ")
  print()

"""

"""
for x in range(n):
  for y in range(x + 1):
    print(' ', end=" ")
  for y in range(x,n):
    print("*", end=" ")
  print()

"""

for x in range(n):
  for y in range(x, n):
    print(' ', end=" ")
  for y in range(x + 1):
    print("*", end=" ")
  for y in range(x):
    print("*", end=" ")
  print()



