# January 2003, Problem 1: Prime Numbers
# https://github.com/v1neethnc/dwite-contest-solutions


# Sieve of Eratosthenes to generate a boolean list where primes are represented by True
def sieve_of_eratosthenes(n): 
	prime = [True for i in range(n+1)] 
	p = 2
	while (p * p <= n): 
		if (prime[p] == True): 
			for i in range(p * p, n+1, p): 
				prime[i] = False
		p += 1
	return prime


with open("../inputs/2003_01_problem1.txt") as file_data:

	# Create list of lists, with each sublist corresponding to a case
	data = [int(i) for i in file_data.read().split("\n")]

	# Save the sieve result and generate the list of primes
	sieve_result = sieve_of_eratosthenes(32767)
	list_primes = [i for i in range(2, len(sieve_result)) if sieve_result[i]]

	# Print the corresponding primes using the input as list index
	for i in data:
		print(list_primes[i-1])
