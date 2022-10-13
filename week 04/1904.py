import sys
from collections import deque

input = sys.stdin.readline

n = int(input())


def tile(n):
    arr = deque([1, 1])

    for _ in range(n - 1):
        arr.append((arr[1] + arr.popleft()) % 15746)

    return arr[1]


print(tile(n))
