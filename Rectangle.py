# Exercise 1 Rectangle Area and Perimeter

length = input("Enter the length of the rectangle: ")
width = input("Enter the width of the rectangle: ")


area = float(length) * float(width)
perimeter = 2 * (float(length) + float(width))

print(f"The area of the rectangle is: {area} cm²")
print(f"The perimeter of the rectangle is: {perimeter} cm")