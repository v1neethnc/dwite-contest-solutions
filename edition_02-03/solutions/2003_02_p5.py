# February 2003, Problem 5: BASE CONVERTER
# https://github.com/v1neethnc/dwite-contest-solutions


# Convert any number in base 2-16 to base 10
def get_base10_val(num, base):
	vals = '0123456789ABCDEF'
	res, exp = 0, 0

	# Iterate from right to left and calculate decimal value
	for i in num[::-1]:
		res += (base ** exp) * vals.find(i) 
		exp += 1
	return res

# Convert decimal number to any base between 2-16
def convert_base10_val(num, base):
	res = ''
	vals = '0123456789ABCDEF'
	while num > 0:
		res = vals[num % base] + res
		num = num // base
	return res

with open("../inputs/2003_02_problem5.txt") as file_data:

	# Create list of lists, with each second sublist corresponding to a case
	data = file_data.read().split("\n")

	# Iterate through the cases
	for i in data:
		vals = i.split(' ')
		v1 = get_base10_val(vals[0], int(vals[1]))
		res = convert_base10_val(v1, int(vals[2]))
		print(res)
