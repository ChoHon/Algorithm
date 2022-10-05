import sys
input = sys.stdin.readline

board = [[7, 2, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0], 
        [6, 1, 0, 0, 4, 0, 0, 0, 3],
        [5, 0, 0, 0, 0, 9, 2, 7, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 3, 6, 8, 0, 0, 0, 0, 4],
        [8, 0, 0, 0, 2, 0, 0, 1, 5],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 9, 6]]

# board = [list(map(int, input().split())) for x in range(9)]

blank = []
for i in range(9):
    blank += [[i, j] for j in range(9) if board[i][j] == 0]

def check(i, j, v):
    for a in range(9):
        if board[i][a] == v:
            return False
        
        if board[a][j] == v:
            return False

    a_weight = i // 3 * 3
    b_weight = j // 3 * 3
    for a in range(3):
        for b in range(3):
            if board[a + a_weight][b + b_weight] == v:
                return False

    return True

def sudoku(k):
    if k == len(blank):
        for i in board:
            for j in i:
                print(j, end=' ')
            print('')
        exit(0)

    else:
        for i in range(1, 10):
            if check(blank[k][0], blank[k][1], i):
                board[blank[k][0]][blank[k][1]] = i
                sudoku(k + 1)
                board[blank[k][0]][blank[k][1]] = 0

sudoku(0)