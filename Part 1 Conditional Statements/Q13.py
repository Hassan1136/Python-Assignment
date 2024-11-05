num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == "+":
    print(num1, "+", num2, "=", num1 + num2)
elif operator == "-":
    print(num1, "-", num2, "=", num1 - num2)
elif operator == "*":
    print(num1, "*", num2, "=", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print(num1, "/", num2, "=", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operator. Please enter one of +, -, *, /.")
