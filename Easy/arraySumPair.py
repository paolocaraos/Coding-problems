#########################################################################
# Problem:
# Given an integer array A[] and a number x, check for pairs in A[] with sum as x
#
# Solution:
# Iterate through the array, and save each element in a hash set
# For each element calculate the pair that would complete the sum.
# If the pair is in the hash set, then a pair is found.
# 
# Key Concepts:
# -set has faster lookup than list
# -Linear time
#########################################################################

import numpy

#returns a list of pairs 
def pairSum(a, k):
	s = set()
	result = []
	for i in range(0, len(a)):
		temp = k - a[i]
		if (temp >= 0  and temp in s):
			result.append((temp, a[i]))
		s.add(a[i])
	return result 

def main():
	array = [0 ,2 ,3, 6, 1, 1, 1, 8, 8]
	sum = 9
	result = pairSum(array, sum)
	for pair in result:
		print(" ", pair, " \n")

if __name__ == "__main__":
    main()