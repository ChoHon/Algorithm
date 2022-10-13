import sys
from collections import deque

input = sys.stdin.readline

n = int(input())


def fibonacci(n):
    arr = [1, 1]
    switch = 1

    for _ in range(n - 2):
        switch = 1 - switch
        arr[switch] = sum(arr)

    return arr[switch]


def fibonacci2(n):
    arr = [1, 1]

    for _ in range(n - 2):
        arr.append(arr[-1] + arr[-2])

    return arr[-1]


print(fibonacci(n))
print(fibonacci2(n))
