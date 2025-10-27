import random
from game_data import data

class Game:
	def __init__(self, compare_name, compare_follower_count, compare_description, compare_country):
		self.name = compare_name;
		self.follower_count = compare_follower_count;
		self.description = compare_description;
		self.country = compare_country;

	def compare(self, other):
		return self.follower_count > other.follower_count
		# if self.follower_count > other.follower_count:
		# 	return True
		# else:
		# 	return False
		
	@staticmethod
	def get_random_game():
		choice = random.choice(data)
		return Game(choice['name'], choice['follower_count'], choice['description'], choice['country'])



def test_game_compare():
	correct = True	
	comparator_b = Game.get_random_game()
	score = 0
	
	while correct:
		comparator_a = comparator_b
		comparator_b = Game.get_random_game()
		
		print(f"Comparator A: {comparator_a.name}, {comparator_a.description} from {comparator_a.country}. VS ")
		print(f"Comparator B: {comparator_b.name}, {comparator_b.description} from {comparator_b.country}.")
		a_or_b = input("Who has more followers? Type 'a' or 'b': ").lower()
		# if a_or_b == 'a' and comparator_a.follower_count >= comparator_b.follower_count:
		# 	score += 1
		# elif a_or_b == 'b' and comparator_a.follower_count <= comparator_b.follower_count:
		# 	score += 1
		# else:
		# 	correct = False
		#   print("Incorrect!")
		if (a_or_b == 'a' and comparator_a.compare(comparator_b)) or (a_or_b == 'b' and comparator_b.compare(comparator_a)):
			score += 1
			print(f"Correct! current score is: {score}")
		else:
			correct = False
			print(f"Sorry, that's wrong. final score is: {score}")
			
			
	play_again = input("Do you want to play again? Type 'y' or 'n': ")
	if play_again == 'y':
		test_game_compare()
	elif play_again == 'n':
		print("Thanks for playing!")

test_game_compare()
