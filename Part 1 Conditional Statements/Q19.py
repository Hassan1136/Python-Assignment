
# 19. Check if a string input is uppercase, lowercase, or a mix.

user_input = input("Enter a string: ")

if user_input.isupper():
    print("The string is uppercase.")
elif user_input.islower():
    print("The string is lowercase.")
else:
    print("The string is a mix of uppercase and lowercase.")