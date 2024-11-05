
# 9. Write a program to print the first 10 Fibonacci numbers.

num = 10
a = 0
b = 1
print(a)
print(b)
for i in range (2, num):
    c = a + b 
    print(c)
    a = b 
    b = c