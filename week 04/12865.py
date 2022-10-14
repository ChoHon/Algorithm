import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for x in range(n)]


def backpack(arr, k):
    dp = [0] * (k + 1)
    for stuff in arr:
        for i in range(k, stuff[0] - 1, -1):
            dp[i] = max(dp[i], dp[i - stuff[0]] + stuff[1])

    return dp[-1]


print(backpack(arr, k))

"""
4 7
6 13
4 8
3 6
5 12
"""
