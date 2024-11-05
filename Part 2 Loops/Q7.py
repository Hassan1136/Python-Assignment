
# 7. Find the factorial of a number using a `while` loop.

num = int(input("Enter an number: "))
factorial = 1
i = 1

if num < 0:
    print("Factorial does not exist for negative number.")
elif num == 0:
    print("Factorial of 0 is 1.")
else:
    while i <= num:
        factorial = factorial * i
        i += 1
    print("Factorial of", num, "is", factorial)