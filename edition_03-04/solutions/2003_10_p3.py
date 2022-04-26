# October 2003, Problem 3: QWERTY Keyboard Decoder
# https://github.com/v1neethnc/dwite-contest-solutions


with open("../inputs/2003_10_problem3.txt") as file_data:

	# Create list of lists, with each second sublist corresponding to a case
	data = file_data.read().split("\n")

	# QWERTY order and corresponding decoded letters
	qwerty_order = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
	new_letters = "opqwertyuiklasdfghjnmzxcvbOPQWERTYUIKLASDFGHJNMZXCVB"
	
	# Iterate through the cases
	for case in data:
		res = ''
		for i in case:
			if i in qwerty_order:
				res += new_letters[qwerty_order.index(i)]
			else:
				res += i
		print(res)
