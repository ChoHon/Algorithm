import sys

input = sys.stdin.readline
INF = sys.maxsize

t = int(input())


def merge_files():
    n = int(input())
    file = list(map(int, input().split()))

    dp = [[0] * n for x in range(n)]
    sum = [0]

    for f in file:
        sum.append(sum[-1] + f)

    for d in range(1, n):
        for i in range(n - d):
            j = i + d
            dp[i][j] = INF

            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + sum[j + 1] - sum[i])

    print(dp[0][n - 1])


for x in range(t):
    merge_files()
