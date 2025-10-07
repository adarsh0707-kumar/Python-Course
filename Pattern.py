n = int(input("Enter number of rows: "))

# Print square pattern
"""
for x in range(n):
  for y in range(n):
    print("symbol", end=" ")
  print()

"""
# Print right angle triangle pattern
"""

for x in range(n):
  for y in range(x+1):
    print("*", end=" ")
  print()

"""
# Print inverted right angle triangle pattern
"""

for x in range(n):
  for y in range(x, n):
    print("*", end=" ")
  print()

"""
# Print pyramid pattern
"""
for x in range(n):
  for y in range(x+1):
    print('', end=" ")
  for x in range(x, n):
    print("*", end=" ")

  print()
"""
# Print inverted pyramid pattern
"""
for x in range(n):
  for y in range(x, n):
    print('', end=" ")
  for x in range(x +1):
    print("*", end=" ")

  print()

"""
# Print Right Triangle Star Pattern
"""
for x in range(n):
  for y in range(x,n):
    print(' ', end=" ")
  for y in range(x + 1):
    print("*", end=" ")
  print()

"""
# Print Inverted Left Triangle Star Pattern
"""
for x in range(n):
  for y in range(x + 1):
    print(' ', end=" ")
  for y in range(x,n):
    print("*", end=" ")
  print()

"""
# hill pattern
"""
for x in range(n):
  for y in range(x, n):
    print(' ', end=" ")
  for y in range(x + 1):
    print("*", end=" ")
  for y in range(x):
    print("*", end=" ")
  print()


"""
# Reverse hill pattern
"""
for x in range(n):
  for y in range(x +1):
    print(' ', end=" ")
  for y in range(x, n):
    print("*", end=" ")
  for y in range(x,n-1):
    print("*", end=" ")
  print()
"""

# diamond pattern
"""
for x in range(n-1):
  for y in range(x, n):
    print(" ", end=" ")
  for y in range(x + 1):
    print("*", end=" ")
  for y in range(x):
    print("*", end=" ")
  print()
for x in range(n):
  for y in range(x +1):
    print(" ", end = " ")
  for y in range(x, n):
    print("*", end=" ")
  for y in range(x,n-1):
    print("*", end=" ")
  print()
"""