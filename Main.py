# Variable = A container for a value ( string, integer, float, boolean)
# A variable behaves as the value that it contains

#Strings
first_name = "Adarsh"
food = "Pizza"
email = "Adarsh@example.com"

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")

#Integer
age = 21
quantity = 3
num_of_students = 50

print(f"You are {age} years old")
print(f"You have ordered {quantity} items")
print(f"There are {num_of_students} students in the class")

#Float
price = 9.99
gpa = 3.5
distance = 12.7

print(f"The price is {price}")
print(f"Your GPA is {gpa}")
print(f"The distance is {distance} km")

#Boolean
is_student = True
for_sale = False

print(f"Are you a student? {is_student}")
print(f"Is the item for sale? {for_sale}")


# Typecasting = Converting the data type of a value to another data type  str(), int(), float(), bool()

name = "Adarsh Kumar"
age = 21
gpa = 3.5
is_student = True

print(type(name))      # str
print(type(age))       # int
print(type(gpa))       # float
print(type(is_student)) # bool

# Typecasting
age = str(age)         # int to str
gpa = int(gpa)         # float to int
is_student = str(is_student) # bool to Strings
print(age)       # str
print(gpa)       # int
print(is_student) # str
