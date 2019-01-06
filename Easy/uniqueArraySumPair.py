#########################################################################
# Problem:
# Given an integer array A[] and a number x, check for pairs in A[] with sum as x
# print the unique pairs only
#
# Solution:
# Iterate through the array, and save each element in a hash set
# For each element calculate the pair that would complete the sum.
# if the pair is in the hash set. Then a pair is found.
# The final list must then be rid of duplicates
# 
# Key Concept:
# -Removing duplicates in a list
# -Linear time
#########################################################################

import numpy

#returns a list of pairs 
def pairSum(a, k):
	s = set()
	knownPairs = set()
	for i in range(0, len(a)):
		temp = k - a[i]
		if (temp >= 0  and temp in s):
			if temp >= a[i]:
				pair = (a[i], temp)
			else:
				pair = (temp, a[i])
			if pair not in knownPairs:
				knownPairs.add((temp, a[i]))
		s.add(a[i])		
	return list(knownPairs)

def main():
	array = [0 ,2 ,3, 6, 1, 1, 1 , 8, 8]
	sum = 8
	result = pairSum(array, sum)
	for pair in result:
		print(" ", pair, " \n")

if __name__ == "__main__":
    main()