import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for x in range(n)]

def check(n, arr, x, y):
    for i in range(n):
        for j in range(n):
            if arr[i + x][j + y] != arr[x][y]:
                return False

    return True

def colored_paper(n, arr, x, y):
    anw = [0, 0]
    
    if check(n, arr, x, y):
        anw[arr[x][y]] += 1

        return anw
    else:
        anw = [x+y for x, y in zip(anw, colored_paper(n//2, arr, x, y))]
        anw = [x+y for x, y in zip(anw, colored_paper(n//2, arr, x + n//2, y))]
        anw = [x+y for x, y in zip(anw, colored_paper(n//2, arr, x, y + n//2))]
        anw = [x+y for x, y in zip(anw, colored_paper(n//2, arr, x + n//2, y + n//2))]

    return anw

for i in colored_paper(n, arr, 0, 0):
    print(i)