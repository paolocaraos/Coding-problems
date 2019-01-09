#
#	Problem :
#
#		You are a professional robber planning to rob houses along a street. 
#		Each house has a certain amount of money stashed, the only constraint 
#		stopping you from robbing each of them is that adjacent houses have 
#		security system connected and it will automatically contact the police
#		if two adjacent houses were broken into on the same night.
#
#		Given a list of non-negative integers representing the amount of money 
#		of each house, determine the maximum amount of money you can rob tonight 
#		without alerting the police.
#
#	Example:
#		Input: [1,2,3,1]
#		Output: 4
#		Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#             Total amount you can rob = 1 + 3 = 4.: 
#
#
#	Solution:
#		-Have an even sum and an odd sum for the array
#		-The output is the greater of the two
#		

def maxProfit(houses):
	profit = [ 0, 0 ]
	for i in range(0, len(houses)):
		profit[i % 2] += houses[i]
	return profit[0] if profit[0] > profit[1] else profit[1]

def main():
	houses = [1, 2, 3, 2]
	print(houses)
	print("Result = ", maxProfit(houses))
	print("Expected = 4")

	houses = [1, 2, 3, 2, 2]
	print(houses)
	print("Result = ", maxProfit(houses))
	print("Expected = 6")

if __name__ == "__main__":
    main()