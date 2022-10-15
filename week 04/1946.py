import sys

input = sys.stdin.readline

t = int(input())


def new(t):
    for _ in range(t):
        n = int(input())
        arr = [list(map(int, input().split())) for x in range(n)]

        arr.sort()
        cnt = 1
        min_score = arr[0][1]

        for temp in arr[1:]:
            if min_score > temp[1]:
                min_score = temp[1]
                cnt += 1

        print(cnt)


new(t)

"""
2
5
3 2
1 4
4 1
2 3
5 5
7
3 6
7 3
4 2
1 4
5 7
2 5
6 1
"""
