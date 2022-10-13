import sys
from collections import deque

input = sys.stdin.readline

t = int(input())


def coin(t):
    for _ in range(t):
        n = int(input())
        arr = deque(map(int, input().split()))
        m = int(input())

        dp = [0] * (m + 1)
        dp[0] = 1

        for c in arr:
            for i in range(1, m + 1):
                if i - c >= 0:
                    dp[i] += dp[i - c]

        print(dp[m])


coin(t)
