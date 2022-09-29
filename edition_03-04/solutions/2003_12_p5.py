# December 2003, Problem 5: Sum of Two Prime Numbers
# https://github.com/v1neethnc/dwite-contest-solutions


def sieve_of_eratosthenes(n: int) -> list: 

	"""
	Function to return a descending list of primes for a given input.

	Parameters:
		n:				(int) upper limit on the maximum prime

	Returns:
		primes_list:	(list) list containing primes until n 
	"""

	# Tracking primes using index
	prime = [True for i in range(n+1)] 
	p = 2

	# Running the sieve
	while (p * p <= n): 
		if (prime[p] == True): 
			for i in range(p * p, n+1, p): 
				prime[i] = False
		p += 1
	prime[0], prime[1] = False, False
	
	# Creating the list of primes
	primes_list = [ind for ind in range(0, len(prime)) if prime[ind] == True]
	return primes_list[::-1]


def is_prime_sum(num: int, primes: list) -> bool:
	
	"""
	Function to calculate if the given number can be expressed as a sum of primes

	Parameters:
		num:	(int) the number to check
		primes:	(list) the list of primes until num

	Returns:
		res:	(bool) True if num can be expressed as a sum of primes, False otherwise
	"""

	for i in primes:
		if num - i in primes:
			return True
	return False


with open("../inputs/2003_12_problem5.txt") as file_data:

	# Create list from file
	data = [int(i) for i in file_data.read().split('\n')]
	
	# Iterate through the inputs
	for line in data:
		lst_primes = sieve_of_eratosthenes(line)
		
		# Checks the primes and tests the prime sum condition
		for val in lst_primes:
			if is_prime_sum(val, lst_primes):
				print(val)
				break
