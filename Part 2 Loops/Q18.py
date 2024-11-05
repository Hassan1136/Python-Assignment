
# 18. Use a loop to print numbers in reverse order within a given range.

start = int(input("Enter a number: "))
end = int(input("Enter a number: "))

if start > end:
    start, end = end, start

for i in range (end, (start - 1), -1):
    print(i)