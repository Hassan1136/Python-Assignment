
# 20. Create a program that evaluates if an inputted number is prime.

import math

num = int(input("Enter a number: "))
sqrt = int(math.sqrt(num))

if num <= 1:
    print(num, "is not a prime number.")
else:
    is_prime = True
    for i in range(2, sqrt + 1):
        if num % i == 0:
            print(num, "is not a prime number.")
            is_prime = False
            break
    if is_prime:
        print(num, "is a prime number.")
