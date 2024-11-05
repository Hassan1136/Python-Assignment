
# 8. Create a program that checks if a given string is a palindrome.

string = input("Enter a string: ")
reversed_string = string[:: -1]

if reversed_string == string :
    print(string, "is a palindrome.")
else:
    print(string, "is not a palindrome.")