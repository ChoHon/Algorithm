import sys
input = sys.stdin.readline

n = int(input())
board = [[' ' for x in range(2 * n - 1)] for y in range(n)]

def star(n, x, y):
    if n == 3:
        for i in range(5):
            board[2 + x][i + y] = '*'
        for i in range(1, 4, 2):
            board[1 + x][i + y] = '*'
        board[0 + x][2 + y] = '*'
    else:
        star(n//2, x + n//2, y)
        star(n//2, x + n//2, y + n)
        star(n//2, x, y + n//2)

star(n, 0, 0)
for i in board:
    print(''.join(i))
