
# 12. Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot.

temp = int(input("Enter the temperature: "))

if temp <= 0:
    print("Freezing")
elif temp > 0 and temp <= 25:
    print("Moderate")
else:
    print("Hot")