import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
q_arr = [list(map(int, input().split())) for x in range(m)]


def palindrome(arr, q_arr):
    dp = [[0] * (n + 1) for x in range(n + 1)]

    for n_len in range(n):
        for start in range(1, n - n_len + 1):
            end = start + n_len

            if n_len == 0:
                dp[start][end] = 1

            if arr[start - 1] == arr[end - 1]:
                if start + 1 > end - 1:
                    dp[start][end] = 1

                elif dp[start + 1][end - 1]:
                    dp[start][end] = 1

    for s, e in q_arr:
        print(dp[s][e])

    return


palindrome(arr, q_arr)
