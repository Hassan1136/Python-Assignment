
# 13. Use nested loops to print a pyramid pattern of `*`.

n = int(input("Enter a number: "))

for num in range(1,n + 1):
    for i in range(num):
        print ("*", end = " ")
    print()