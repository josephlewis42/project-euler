#!/usr/bin/env python

'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


'''

import itertools


digits = "0123456789"

# alright, we know the prefix is the same for each permuatation of the rear.
# I'm pretty sure permutation numbers are factorials, so that's a good place to
# start, find the largest factorial below 1 mil, that's the number of digits
# we'll need to permute, then we can iterate down.


number_left = 1000000

def permute(prefix, suffix):
	global number_left
	if len(suffix) == 1:
		number_left -= 1
		#print "{} - {}".format(number_left, prefix + "".join(suffix))
		if number_left == 0:
			print prefix + "".join(suffix)
			exit(0)
	else:
		for i in sorted(suffix):
			all_digits = set(suffix)
			all_digits.remove(i)
			
			permute(prefix + i, list(all_digits))

permute("", digits)
