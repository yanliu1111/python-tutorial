from random import randint
# Create global variables
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check users' guess against the answer
def check_answer(user_guess, actual_answer):
    if user_guess > actual_answer:
        print("Too high.")
    elif user_guess < actual_answer:
        print("Too low.")
    else:
        print(f"Correct! The answer was {actual_answer}.")

# Function to set difficulty level
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

print('Welcome to the Number Guessing Game!')
print('I am thinking of a number between 1 and 100.')
answer = randint(1, 100)

# Let the user make a guess
guess = int(input('Make a guess: '))
turns = set_difficulty()
print(f'you have {turns} attempts to guess the number.')


# Track the number of turns and reduce by 1 if they get it wrong

# Repeat the guessing functionality if they get it wrong