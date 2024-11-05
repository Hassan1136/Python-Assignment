
# 15. Print the sum of even and odd numbers separately up to a given number.

num = int(input("Enter a number: "))
even_sum = 0
odd_sum = 0

for i in range (1, num + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("sum of even numbers are: ", even_sum)
print("sum of odd numbers are: ", odd_sum)