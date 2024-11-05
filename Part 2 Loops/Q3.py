
# 3. Write a program to calculate the sum of all numbers between 1 and 100.

num = 0

for i in range (1, 101):
    num += i
    print(num, "when i =", i, )
print("The sum of all numbers =", num)