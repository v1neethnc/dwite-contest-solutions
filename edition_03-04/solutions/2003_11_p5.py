# November 2003, Problem 5: Resistor Colour Code
# https://github.com/v1neethnc/dwite-contest-solutions


with open("2003_11_problem5.txt") as file_data:

	# Create list from file and initialize the index to read from data
	data = file_data.read().split('\n')

	# Create the dictionary to calculate resistance
	clr_val_map = {"BLACK": 0, "BROWN": 1, "RED": 2, "ORANGE": 3, "YELLOW": 4, "GREEN": 5, "BLUE": 6, "VIOLET": 7, "GREY": 8, "WHITE": 9}
	
	# Iterate through the list with a step of 3
	for ind in range(0, len(data), 3):

		# Update the exponent and the resistance value
		exp = clr_val_map[data[ind + 2]] if clr_val_map[data[ind + 2]] < 8 else 0
		val = (clr_val_map[data[ind]] * 10 + clr_val_map[data[ind + 1]]) * (10 ** exp)
		
		# Check if resistance is on the scale of 10**6
		if val // 1000000 > 0:
			print(f"{val // 1000000} Mohms")
		
		# Check if resistance is on the scale of 10**3
		elif val // 1000 > 0:
			print(f"{val // 1000} kohms")
		
		# Print the resistance as ohms
		else:
			print(f"{val} ohms")
