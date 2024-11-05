
# 10. Use a loop to count the number of digits in an integer.

num = int(input("Enter a number: "))
i = 0

while num > 0:
    num = num // 10
    i += 1
print("The total number of digits in the given integer is ", i)