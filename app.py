# import
import random

#welcome message
print("✨✨ Welcome to Number Guessing Game ✨✨")

# function for gussing number
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number :
        guess = int(input(f"Guess a Number between 1 and {x}: "))
        if guess < random_number:
            print(f"😞Sorry, guess again.Number {guess} is too low.")
        elif guess > random_number:
            print(f"💔Sorry, guess again.Number {guess} is too high.")

    print(f"🎊 Congratulation, You Won the Game by choosing Number {random_number} correctly.🎉")

# function for gussing number by computer

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c" and low != high :
        if low != high:
            guess = random.randint(low, high)
        else :
            guess = low    
        feedback = input(f"If {guess} too high (H),too low (L),or Correct (C)??").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback =="l":
            low = guess + 1

    print(f"🥳 Congratulations,Computer guess the Correct Number.It's Number {guess} ✨")

# Run the functions
computer_guess(100)
guess(10)