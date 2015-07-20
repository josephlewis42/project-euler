#!/usr/bin/env pypy

'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

'''
import collections
import itertools

def sieve_of_eratosthenes(maximum_number):
	'''Finds all primes < the maximum_number provided.
	
	'''
	primes = set()
	not_primes = set()
	
	for i in xrange(2, maximum_number):
		if i in not_primes:
			continue
		
		# add this number to the set of primes
		primes.add(i)
		
		# remove all primes afterward.
		for j in xrange(i, maximum_number, i):
			not_primes.add(j)
			
	return primes

# Make sure the sive works.
PRIMES_LT_100 = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 
                     53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
assert PRIMES_LT_100 == sieve_of_eratosthenes(100)

ONE_MIL_PRIMES = sieve_of_eratosthenes(1000000)

def get_rotations(number):
	''' Gets all numerical rotations of a number, e.g. 1234, 2341, 3412, 4123
	
	Computes by taking substrings of a double length string of the input, like
	the dynamic maximal string alignment problem.
	'''
	string = str(number)
	doubled = string * 2
	
	return [doubled[i:i + len(string)] for i in range(len(string))]
	


# A map of string -> occurence counter.
# we know all numbers in a prime are also primes if the int == length of the key
prime_count = collections.defaultdict(int)

for index, prime in enumerate(ONE_MIL_PRIMES):
	print float(index) / len(ONE_MIL_PRIMES)
	
	for i in get_rotations(prime):
		prime_count[i] += 1



total = 0
for prime, count in prime_count.items():
	if len(prime) == count:
		total += 1

print total
