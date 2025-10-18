import random

def deal_card():
  '''Returns a random card from the deck.'''
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  total = sum(cards)
  if total == 21 and len(cards) == 2:
    return 0
  if 11 in cards and total > 21:
    cards.remove(11)
    cards.append(1)
  return total
# order of checks matters
def compare(u_score, c_score):
  if u_score == c_score:
    return "It's a draw!"
  elif c_score == 0:
    return "Computer has a Blackjack! You lose."
  elif u_score == 0:
    return "You have a Blackjack! You win!"
  elif u_score > 21:
    return "You went over. You lose."
  elif c_score > 21:
    return "Computer went over. You win!"
  elif u_score > c_score:
    return "You win!"
  else:
    return "You lose."



def blackjack():
  # print logo
  user_cards = []
  computer_cards = []
  computer_score = -1
  user_score = -1
  game_over = False

  for _ in range(2):
    new_card = deal_card()
    user_cards.append(new_card)
    computer_cards.append(new_card)
  print(user_cards)



  while not game_over:  
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"User cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == 'y':
        new_card = deal_card()
        user_cards.append(new_card)
        # print(user_cards)
      else:
        game_over = True

  while computer_score != 0 and computer_score < 17:
    new_card = deal_card()
    computer_cards.append(new_card)
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score)) 

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
  print ("\n" * 20)
  blackjack()