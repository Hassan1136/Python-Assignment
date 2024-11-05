
# 17. Write a program that continues to ask for a number until the correct number is guessed.

target_number = 11

while True:
        guess = int(input("Guess the number: ")) 
    
        if guess == target_number:
            print("Congratulations! You guessed the correct number!") 
            break
        else:
              print("Try Again!")