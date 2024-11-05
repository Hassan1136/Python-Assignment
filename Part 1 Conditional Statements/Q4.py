
# 4. Take an integer and check if it’s even or odd.

num = int(input("Enter a number: "))

if num <= 0:
    print(num, "is an invalid number.")
elif num > 0 and num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")