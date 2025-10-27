# display art
# from art import logo, vs
from game_data import data
import random

# format the account data into printable format
def format_data(account):
  account_name = account['name']
  account_descr = account['description']
  account_country = account['country']
  return print(f"Compare A: {account_name}, a {account_descr}, from {account_country}.")

def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == 'a' #return True if guess is 'a', else False
  else:
    return guess == 'b' #return True if guess is 'b', else False
# print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
while game_should_continue:
  # generate a random account from the game data
  account_a = random.choice(data)
  account_b = random.choice(data)
  account_a = account_b
  account_b = random.choice(data)

  print(f"Compare A: {format_data(account_a)}")
  print("vs")
  print(f"Against B: {format_data(account_b)}")

  # ask user for a guess
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  # clear()
  print("\n"*20)
  # check if user is correct
  ## - get follower count of each account
  a_followers = account_a['follower_count']
  b_followers = account_b['follower_count']

  ## - use if statement to check if user is correct
  is_correct = check_answer(guess, a_followers, b_followers)

  # give user feedback on their guess

  if is_correct:
    score += 1
    print(f"You are right! current score is: {score}")
  else:
    print(f"Sorry, that's wrong. final score is: {score}")
    game_should_continue = False


# make the game repeatable

# Making account at position B become the next account at position A