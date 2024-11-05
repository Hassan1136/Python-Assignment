
# 15. Write a program to check if a number is within a specified range.

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
your_num = int(input("Enter a your number: "))

if start > end:
    start, end = end, start
    
if your_num in range(start, end+1):
    print(your_num, "is within a given range")
else:
    print(your_num, "is outside a given range")