# From Hackerrank "Bot saves princess -2"
#
# In this version of "Bot saves princess", 
# Princess Peach and bot's position are randomly set. 
# Can you save the princess?
#
# Task:
# 
# Complete the function nextMove which takes in 4 parameters - 
# an integer N, integers r and c indicating the row & column 
# position of the bot and the character array grid - and outputs 
# the next move the bot makes to rescue the princess.
#
# Input:
#
# The first line of the input is N (<100), the size of the board 
# (NxN). The second line of the input contains two space separated 
# integers, which is the position of the bot.
#
# Grid is indexed using Matrix Convention
#
# The position of the princess is indicated by the character 'p' 
# and the position of the bot is indicated by the character 'm' 
# and each cell is denoted by '-' (ascii value: 45).
#
# Output:
# 
# A list of string commands "LEFT" , "RIGHT", "UP", "DOWN"

def nextMove(n,r,c,grid):
    princess = []
    for i in range(0,n):
        for j in range(0, n):
            if(grid[i][j] == 'p'):
                princess = [i,j]
    
    delta_row = princess[0] - r
    delta_col = princess[1] - c
    if(delta_row > 0):
        return "DOWN"
    elif(delta_row < 0):
        return "UP"
    elif(delta_col > 0):
        return "RIGHT"
    elif(delta_col < 0):
        return "LEFT"
    return "PRINCESS FOUND"

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))