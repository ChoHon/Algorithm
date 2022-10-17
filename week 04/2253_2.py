import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
arr = [int(input()) for x in range(m)]


def jumping(arr):
    # n칸에서 최대 속도
    def max_jump(n):
        return int((n * 2) ** 0.5) + 1

    dp = [[INF] * (max_jump(n) + 1) for x in range(n + 1)]
    # 처음에는 한 칸 밖에 점프하지 못하기 때문에
    # dp[2][1]만 만들어야함
    dp[1][0] = 0

    for i in range(2, n + 1):
        if i in arr:
            continue

        for j in range(1, max_jump(i)):
            # 가속, 유지, 감속의 경우 중 작은 값 + 1
            dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1

    temp = min(dp[n])
    return temp if temp < INF else -1


print(jumping(arr))
