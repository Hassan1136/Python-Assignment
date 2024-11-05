
# 14. Write a program that breaks the loop when a certain condition is met.

num = int(input("Enter a number: "))

for i in range (num + 1):
        if num == i:
            print("Condition is met.")
            break
        else:
              print("The program is in progress.")