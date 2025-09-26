#print("Hello World") 
# Day 3 - if/else statements
# print('welcome to the rollercoaster!')
# height = int(input('What is your height in cm? '))
# if height >= 120:
#   print('You can ride the rollercoaster!')
#   age = int(input('What is your age? '))
#   if age < 12:
#     print('Please pay $5.')
#   elif age <= 18:
#     print('Please pay $7.')
#   else:
#     print('Please pay $12.')
# else:
#   print('Sorry, you have to grow taller before you can ride.')

# import random
# random_integer = random.randint(1, 10)
# print(random_integer)

# for number in range(1, 100):
#   if number % 3 == 0 and number % 5 == 0:
#       print("FizzBuzz")
#   elif number % 3 == 0:
#       print("Fizz")
#   elif number % 5 == 0:
#       print("Buzz")
#   else:
#       print(number)

# def my_function():
#   print("Hello")
#   print("Bye")

# my_function()
import random
import hangman_words
from hangman_art import stages, logo, logowin
lives = 6
print(logo)
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
# guess = input("Guess a letter: ").lower()
# print(guess)
# for letter in chosen_word:
#   # print(letter)
#   if letter == guess:
#     print("Right")
#   else:
#     print("Wrong")

placeholder = ""
for position in range(len(chosen_word)):
  placeholder += "_"
print(placeholder)
# for letter in chosen_word:
# guess = input("Guess a letter: ").lower()
# for position in range(len(chosen_word)):
#   letter = chosen_word[position]
#   if letter == guess:
#     placeholder = placeholder[:position] + letter + placeholder[position + 1:] # string slicing, :position means up to but not including position, position + 1: means from position + 1 to the end
# print(placeholder)

# method1
game_over = False
while not game_over:
  print(f"**************** {lives}/6 LIVES LEFT****************")
  guess = input("Guess a letter: ").lower()

  if guess in placeholder:
    print(f"You've already guessed {guess}")

  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      placeholder = placeholder[:position] + letter + placeholder[position + 1:] # string slicing, :position means up to but not including position, position + 1: means from position + 1 to the end
  print(placeholder)

  if guess not in chosen_word:
    lives -= 1
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    if lives == 0:
      game_over = True
      print('****************IT WAS {chosen_word}! YOU LOSE****************')

  if '_' not in placeholder:
    game_over = True
    print('****************YOU WIN****************')
    
  if not game_over:
    print(stages[lives])
  else:
    if lives > 0:
      print(logowin)
    else:
      print(logo)
# method2
# corret_letters = []
# game_over2 = False
# while not game_over2:
#   guess = input("Guess a letter: ").lower()
#   placeholder2 = ""
#   for letter in chosen_word:
#     if letter == guess:
#       placeholder2 += letter 
#       print("Right", placeholder2)
#       corret_letters.append(letter)
#     elif letter in corret_letters:
#       placeholder2 += letter
#     else:
#       placeholder2 += "_"
#   print(placeholder2)
#   if '_' not in placeholder2:
#     game_over2 = True
#     print("You win.")