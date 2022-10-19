import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for x in range(n)]
dp = [0] * (n + 1)


def resignation(n):
    for i in range(1, n + 1):
        dp[i] = max(dp[i], dp[i - 1])

        finish = i + arr[i - 1][0] - 1
        if finish <= n:
            dp[finish] = max(dp[finish], dp[i - 1] + arr[i - 1][1])

    return dp[n]


print(resignation(n))
