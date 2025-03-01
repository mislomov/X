#1.Given a side of square. Find its perimeter and area.

side = int(input("Enter the side of the square: "))
area = side ** 2
perimeter = 4*side

print("Area of square: ", area)
print("Perimeter of square: ", perimeter)

# 2. Given diameter of circle. Find its length.

diametr = int(input("Enter the diametr of the circle: "))
pi = 3.14159
length = pi * diametr

print("Length of the circle is: ", length)

# 3.Given two numbers a and b. Find their mean.

a = int(input("Enter number 'a': "))
b = int(input("Enter number 'b': "))

mean = (a+b)/2

print("Mean of a and b equals to: ", mean)

# 4.Given two numbers a and b. Find their sum, product and square of each number.

a = int(input("Enter number 'a': "))
b = int(input("Enter number 'b': "))

sum = a+b
product = a*b
square_of_a = a**2
square_of_b = b**2

print("Sum of a and b: ", sum)
print("Product of a and b: ", product)
print("Square of a: ", square_of_a)
print("Square of b: ", square_of_b)