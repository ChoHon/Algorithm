import sys

input = sys.stdin.readline

a = input().strip()
b = input().strip()


def longest_part(a, b):
    a_len = len(a)
    b_len = len(b)
    arr = [[0] * (b_len + 1) for x in range(a_len + 1)]
    max_length = 0

    for i in range(1, a_len + 1):
        for j in range(1, b_len + 1):
            if a[i - 1] == b[j - 1]:
                arr[i][j] = arr[i - 1][j - 1] + 1
                if max_length < arr[i][j]:
                    max_length = arr[i][j]
                    location = i

    return max_length, a[location - max_length : location]


for temp in longest_part(a, b):
    print(temp)

"""
CBBBCC
BCBBBC
"""
