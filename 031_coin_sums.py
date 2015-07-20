#!/usr/bin/env pypy

'''
In England the currency is made up of pound, (pound), and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, (pound)1 (100p) and (pound)2 (200p).
It is possible to make (pound)2 in the following way:

1*(pound)1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p
How many different ways can (pound)2 be made using any number of coins?
'''

DESIRED_VALUE_P = 200  # The desired value in pence

# This feels a variant of the SUBSET-SUM problem, unfourtinately that is 
# NP-Complete, however we do have an infinite number of coins; so that can 
# help us and should make this tractable.

# add all the possible values of each denomination going into 2 pounds
denominations = [200, 100, 50, 20, 10, 5, 2, 1]

# we're going to do this "cleverly" by going from highest to lowest values so we
# don't waste time on things that add up too many times.

def recursive_fill(denominations, value):
	# goal met
	if value == 0:
		return 1
	
	# we've run out of options
	if len(denominations) == 0 or value < 0:
		return 0
	
	denomination = denominations[0]
	rest         = denominations[1:]
	
	total = 0
	for amount in xrange(0, value + 1, denomination):
		total += recursive_fill(rest, value - amount)
	
	return total

print recursive_fill(denominations, DESIRED_VALUE_P)
