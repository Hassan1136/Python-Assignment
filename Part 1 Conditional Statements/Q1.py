
# 1. Write a program that checks if a given number is positive, negative, or zero.

num = int(input("Enter a number: "))

if num > 0:
    print(num, "is a positive number.")
elif num < 0:
    print(num, "is a negative number.")
else:
    print(num, "is zero.")