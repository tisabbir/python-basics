import random

def guess_the_number():
    print("Guess the Number!")
    secret_number = random.randint(1, 100)
    
    for i in range(10): 
        guess = int(input("Guess a number between 1 and 100: "))

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number!")
            return
    
    print(f"Sorry, you didn't guess the number. It was {secret_number}.")

guess_the_number()
