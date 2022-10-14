import sys

input = sys.stdin.readline

a = input().strip()
b = input().strip()


def lcs(a, b):
    a_len = len(a)
    b_len = len(b)
    arr = [[0] * (a_len + 1) for x in range(b_len + 1)]

    for i in range(1, a_len + 1):
        for j in range(1, b_len + 1):
            if a[i - 1] == b[j - 1]:
                arr[i][j] = arr[i - 1][j - 1] + 1
            else:
                arr[i][j] = max(arr[i][j - 1], arr[i - 1][j])

    return arr[a_len][b_len]


def lcs2(a, b):
    a_len = len(a)
    b_len = len(b)
    arr = [0] * b_len

    for i in range(a_len):
        cnt = 0
        for j in range(b_len):
            if cnt < arr[j]:
                cnt = arr[j]
            elif a[i] == b[j]:
                arr[j] = cnt + 1

    return max(arr)


print(lcs(a, b))
print(lcs2(a, b))

"""
XXXXXF
XFXXXQ
"""
