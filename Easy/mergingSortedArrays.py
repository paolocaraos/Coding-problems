#########################################################################
# Problem:
# You are given two sorted arrays, A and B, where A has a large enough buffer at the
# end to hold B. Write a method to merge B into A in sorted order.
#
# Solution:
# -Have two iterators going through both A and B
# -Find gaps in A where segments of B can fit
#
# Key Concepts:
# -iterators
# -inserting subarrays
#########################################################################

import numpy
import sys

def merge(a, b):
	totalLength = len(a) + len(b)
	if len(a) == 0:
		return b
	j = 0
	for i in range(0, totalLength):
		while (j < len(b) and a[i] > b[j]):
			a.insert(i, b[j])
			j+=1
			i+=1
	return a

def main():
	a = [0,2, 44, 67, 88, 90]
	b = [1, 5, 7,9, 23, 70]
	expected = [0, 1, 2, 5 , 7, 9, 23, 44, 67, 70, 88, 90]
	result = merge(a, b)
	print("Result: ")
	print(result)
	print("Success:", set(expected) == set(result))

	a = [90]
	b = [1, 5, 7,9, 23, 70]
	expected = [1, 5 , 7, 9, 23, 70,90]
	result = merge(a, b)
	print("Result: ")
	print(result)
	print("Success:", set(expected) == set(result))

	a = [90]
	b = []
	expected = [90]
	result = merge(a, b)
	print("Result: ")
	print(result)
	print("Success:", set(expected) == set(result))

	a = []
	b = [90]
	expected = [90]
	result = merge(a, b)
	print("Result: ")
	print(result)
	print("Success:", set(expected) == set(result))

if __name__ == "__main__":
    main()