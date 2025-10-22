from random import randint
# Create global variables
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check users' guess against the answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer again guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:        
        print("Too low.")
        return turns - 1
    else:
        print(f"Correct! The answer was {actual_answer}.")

# Function to set difficulty level
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    #print logo
    print('Welcome to the Number Guessing Game!')
    print('I am thinking of a number between 1 and 100.')
    answer = randint(1, 100)
    print (f'Pssst, the correct answer is {answer}')  # For testing purposes

    turns = set_difficulty()
    print(f'you have {turns} attempts to guess the number.')

    guess = 0
    # Let the user make a guess
    while guess != answer:
        guess = int(input('Make a guess: '))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print('Guess again.')  
		

		

game()


# Track the number of turns and reduce by 1 if they get it wrong

# Repeat the guessing functionality if they get it wrong