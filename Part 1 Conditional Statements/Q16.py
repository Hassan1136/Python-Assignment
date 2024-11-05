
# 16. Take the length of three sides and classify the triangle (equilateral, isosceles, or scalene).

side1 = int(input("Enter the first side of a triangle: "))
side2 = int(input("Enter the second side of a triangle: "))
side3 = int(input("Enter the third side of a triangle: "))

if side1 == side2 == side3:
    print("This is a equilateral triangle")
elif side1 == side2 != side3 or side1 == side3 != side2 or side2 == side3 != side1:
    print("This is a isosceles triangle")
else:
    print("This is scalene triangle")