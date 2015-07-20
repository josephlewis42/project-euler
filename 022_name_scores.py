#!/usr/bin/env python

'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?

'''

names = []

with open("p022_names.txt") as namefile:
	text = namefile.read()
	columns = text.split(",")
	names = [c.strip()[1:-1] for c in columns]  # strip off the quotes
	
names = sorted(names)

# there is an off by 1 error b/c they start numbering at 1, so we'll insert a 
# blank value at 0 to fix this
names = [""] + names

total = 0
for index, name in enumerate(names):
	# find ord of each letter, subtract it from a to get position, add 1 for
	# 0 offset.
	namevals = map(lambda letter: ord(letter) - ord("A") + 1, name)
	namesum = sum(namevals)
	namescore = namesum * index
	
	total += namescore
	
	print "{} - {}".format(name, namescore)

print total
