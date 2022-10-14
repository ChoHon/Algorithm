import sys

input = sys.stdin.readline

n = int(input())


def mul_matrix():
    arr = []
    for i in range(n):
        a, b = map(int, input().split())

        if i == 0:
            arr.append(a)

        arr.append(b)

    dp = [[0 for x in range(n + 1)] for y in range(n + 1)]

    for gap in range(1, n):
        for i in range(1, n - gap + 1):
            dp[i][i + gap] = 1e10
            for k in range(i, i + gap):
                if (
                    dp[i][k] + dp[k + 1][i + gap] + (arr[i - 1] * arr[k] * arr[i + gap])
                    < dp[i][i + gap]
                ):
                    dp[i][i + gap] = (
                        dp[i][k]
                        + dp[k + 1][i + gap]
                        + (arr[i - 1] * arr[k] * arr[i + gap])
                    )

    return dp[1][n]


print(mul_matrix())

"""
3
5 3
3 2
2 6
"""
