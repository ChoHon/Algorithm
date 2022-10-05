# n, m = map(int, input().split())
# arr = [input() for x in range(n)]

n, m = 8, 8
arr = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBBBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']

white_first = ['WBWBWBWB', 'BWBWBWBW'] * 4
blank_first = ['BWBWBWBW', 'WBWBWBWB'] * 4


def check(x, y):
    cnt_w = 0
    cnt_b = 0

    for i in range(8):
        for j in range(8):
            if white_first[i][j] != arr[i + x][j + y]:
                cnt_w += 1

    for i in range(8):
        for j in range(8):
            if blank_first[i][j] != arr[i + x][j + y]:
                cnt_b += 1

    return min(cnt_w, cnt_b)


def chess_board():
    cnt = 65
    for i in range(n-7):
        for j in range(m - 7):
            cnt = min(cnt, check(i, j))

    return cnt

print(chess_board())