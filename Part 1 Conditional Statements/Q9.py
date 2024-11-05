
# 9. Take three sides of a triangle as input and check if they form a valid triangle.

side1 = int(input("Enter the first side of a triangle: "))
side2 = int(input("Enter the second side of a triangle: "))
side3 = int(input("Enter the third side of a triangle: "))


if side1 > 0 and side2 > 0 and side3 > 0:

    if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
        print("This is a valid triangle")
    else:
        print("This is not a valid triangle")
else:
    print("This is not a valid triangle")
