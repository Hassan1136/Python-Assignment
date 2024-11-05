
# 6. Write a program to find the largest of two numbers.

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))

if num1 > num2:
    print(num1, "is greater than ", num2)
elif num1 < num2:
    print(num2, "is greater than ", num1)
else:
    print("Both numbers are equal.")