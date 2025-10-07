# Loop = loop has various types in python
# 1. for loop
# 2. while loop
# 3. nested loop
# 4. loop control statements (break, continue, pass)

# 1. while loop = executes a block of code as long as a condition is true
# syntax:
# while condition:
#     # code to be executed
"""
name = input("Enter your name: ")

while name == "":
  print("You didn't enter your name")
  name = input("Enter your name: ")
print(f"Hello {name}")

"""

# 2.For loops = used to iterate over a sequence (list, tuple, string) or other iterable objects
"""
for x in reversed(range(1,11,2)):
  print(x)
  
"""
for x in range(1, 21):
  if x == 13:
    print("Unlucky")
    continue
  print(x)