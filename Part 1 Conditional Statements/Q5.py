
# 5. Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Your grade is A.")
elif marks >=80:
    print("Your grade is B.")
elif marks >=60:
    print("Your grade is C.")
elif marks >=40:
    print("Your grade is D.")
else:
    print("Your grade is F.")