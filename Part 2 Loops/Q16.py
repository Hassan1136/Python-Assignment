
# 16. Create a program to calculate the sum of the digits of an inputted integer.

num = int(input("Enter a number: "))
sum = 0

while num > 0:
    dig = num % 10
    sum = sum + dig
    num = num // 10
print("The sum of digits of the given integer is: ", sum)