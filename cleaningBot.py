#  Hacker Rank Cleaning Bot Problem
#
#  Given a 2D grid of clean and dirty cells and a starting cell for the bot
#  Provide the next move a bot needs to do to clean the grid in the fewest
#  amount of moves
#
target_locked = False
target = [-1, -1]
def scan(r, c, board):
    scan_radius = 1
    length = len(board[0])
    result = []    
    while(target_locked is False and scan_radius < length):
        result = perimeterScan(board, r, c, scan_radius, length, 'd')
        if(result is not None):
            return result
        scan_radius += 1
    return result

def perimeterScan(arr, r , c ,radius, length, target):#prioritize 4-connected adjacent
    i = 1
    N = [r - radius , c          ]
    E = [r          , c + radius ]
    S = [r + radius , c          ]
    W = [r          , c - radius ]
    indices = [N, E, S, W]
    for index in indices:
        if(index[0] >= 0 and index[0] < length and index[1] >= 0 and index[1] < length):
            if(arr[index[0]][index[1]] == target):
                target_locked = True
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
                    target_locked = True
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
                target_locked = True
                return index

def next_move(posr, posc, board):
    if(board[posr][posc] == 'd'):
        print("CLEAN")
        target_locked = False
        board[posr][posc] = '-'
    else:
        target = scan(posr, posc, board)

        if(target is None):
            return 
        #print(target)
        delta_row = target[0] - posr
        delta_col = target[1] - posc
        if(delta_row > 0):
            print("DOWN")
        elif(delta_row < 0):
            print("UP")
        elif(delta_col > 0):
            print("RIGHT")
        elif(delta_col < 0):
            print("LEFT")

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)