
# 11. Print the reverse of a given number.

num = int(input("Enter a number: "))
rev = 0

while num > 0:
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
print("The reverse of the given number is ", rev)