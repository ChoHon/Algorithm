n = int(input())
board = [[' ' for x in range(n)] for y in range(n)]

def star(n, x, y):
    if n == 1:
        board[x][y] = '*'

    else:
        for i in range(0, n, n//3):
            for j in range(0, n, n//3):
                if (i == n // 3) and (j == n // 3):
                    continue
                star(n // 3, x + i, y + j)

star(n, 0, 0)
for i in board:
    for j in i:
        print(j, end='')
    print('')

