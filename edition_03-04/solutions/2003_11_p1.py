# November 2003, Problem 1: Rock, Paper, Scissors
# https://github.com/v1neethnc/dwite-contest-solutions


# Function to return the winner of the current hand
def check_winner(p1_hand: str, p2_hand: str) -> int:
	
	"""
	Given two hands, return the status of the game.

	Parameters:
		p1_hand: (str) single character representing player 1's hand
		p2_hand: (str) single character representing player 2's hand

	Returns:
		(int) 0 for draw, 1 for player 1 win, 2 for player 2 win
	"""

	hand_map = {'R': 'S', 'P': 'R', 'S': 'P'}
	if p1_hand == p2_hand:
		return 0
	if p2_hand == hand_map[p1_hand]:
		return 1
	if p1_hand == hand_map[p2_hand]:
		return 2

with open("2003_11_problem1.txt") as file_data:

	# Create list of lists, with each second sublist corresponding to a case
	data = [[j for j in i.split()] for i in file_data.read().split("\n")]

	# Go through each case one by one
	for game in data:
		
		# Initialize the counters
		p1_win, p2_win, draw = 0, 0, 0

		# Go through each hand
		for hands in game:

			# Check the winner: 0 for draw, 1 for player 1, 2 for player 2
			game_res = check_winner(hands[0], hands[1])

			# Check result and increase corresponding counter
			if game_res == 1:
				p1_win += 1
				if p1_win == 2:
					print(f"PLAYER ONE {draw}")
					break
			elif game_res == 2:
				p2_win += 1
				if p2_win == 2:
					print(f"PLAYER TWO {draw}")
					break
			else:
				draw += 1
