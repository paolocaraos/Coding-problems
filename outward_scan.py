#	Problem:
#	
#	Given a cell in a 2D matrix. 
#   -Traverse the adjacent cells in a clockwise outward manner.
#   -Traverse in 4-connected order
#


def outwardScan(arr, r, c, radius, length, target):
	curr_radius = 1
	output = []	
	while(curr_radius <= radius):
		output = perimeterScanV3(arr, r, c, curr_radius, length, target)
		if(output is not None):
			return output
		curr_radius += 1
	return output

def perimeterScan(arr, r, c, radius, length):
	output = []
	i = 0
	while(i < radius * 8):
		y = 0
		x = 0
		if(i < radius * 2): #top side
			y = r - radius
			x = c - radius + i
		elif(i >= radius * 2 and i < radius * 4): #right side
			y = r - radius + (i % (radius * 2))
			x = c + radius
		elif(i >= radius * 4 and i < radius * 6): #bot side
			y = r + radius
			x = c + radius - (i % (radius * 2))
		elif(i >= radius * 6): #left side
			y = r + radius - (i % (radius * 2))
			x = c - radius			
		if(y >= 0 and y < length and x >= 0 and x < length):
			#print(arr[y][x], " ")
			output.append(arr[y][x])
		i += 1

	return output

def perimeterScanV2(arr, r , c ,radius, length, target):#prioritize 4-connected adjacent
	output = []
	i = 1
	N = [r - radius , c          ]
	E = [r          , c + radius ]
	S = [r + radius , c          ]
	W = [r          , c - radius ]
	indices = [N, E, S, W]
	for index in indices:
		if(index[0] >= 0 and index[0] < length and index[1] >= 0 and index[1] < length):
			output.append(arr[index[0]][index[1]])

	while(i < radius):
		N  = [r - radius    , c          - i]
		E  = [r          - i, c + radius    ]
		S  = [r + radius    , c          + i]
		W  = [r          + i, c - radius    ]

		N2 = [r - radius    , c          + i]
		E2 = [r          + i, c + radius    ]
		S2 = [r + radius    , c          - i]
		W2 = [r          - i, c - radius    ] 
		indices = [N, N2, E, E2,  W, W2, S, S2]
		for index in indices:
			if(index[0] >= 0 and index[0] < length and index[1] >= 0 and index[1] < length):
				output.append(arr[index[0]][index[1]])
		i += 1

	N[1] = c - radius
	E[0] = r - radius
	W[0] = r + radius
	S[1] = c + radius
	indices = [N, E, W, S]
	for index in indices:
		if(index[0] >= 0 and index[0] < length and index[1] >= 0 and index[1] < length):
			output.append(arr[index[0]][index[1]]) 
	return output

def perimeterScanV3(arr, r , c ,radius, length, target):#prioritize 4-connected adjacent
	output = []
	i = 1
	N = [r - radius , c          ]
	E = [r          , c + radius ]
	S = [r + radius , c          ]
	W = [r          , c - radius ]
	indices = [N, E, S, W]
	for index in indices:
		if(index[0] >= 0 and index[0] < length and index[1] >= 0 and index[1] < length):
			if(arr[index[0]][index[1]] == target):
				return index

	while(i < radius):
		N  = [r - radius    , c          - i]
		E  = [r          - i, c + radius    ]
		S  = [r + radius    , c          + i]
		W  = [r          + i, c - radius    ]

		N2 = [r - radius    , c          + i]
		E2 = [r          + i, c + radius    ]
		S2 = [r + radius    , c          - i]
		W2 = [r          - i, c - radius    ] 
		indices = [N, N2, E, E2,  W, W2, S, S2]
		for index in indices:
			if(index[0] >= 0 and index[0] < length and index[1] >= 0 and index[1] < length):
				if(arr[index[0]][index[1]] == target):
					return index
		i += 1

	N[1] = c - radius
	E[0] = r - radius
	W[0] = r + radius
	S[1] = c + radius
	indices = [N, E, W, S]
	for index in indices:
		if(index[0] >= 0 and index[0] < length and index[1] >= 0 and index[1] < length):
			if(arr[index[0]][index[1]] == target):
				return index 

def main():
	arr = [[ 0,  1,  2,  3,  4],
		   [ 5,  6,  7,  8,  9],
		   [10, 11, 12, 13, 14],
		   [15, 16, 17, 18, 19],
		   [20, 21, 22, 23, 24]]
	target = 24
	result = outwardScan(arr, 2, 2, 2, 5, target)
	print(result)

	print("Off center test")
	print(outwardScan(arr, 0, 0, 4, 5, target))

if __name__ == "__main__":
    main()