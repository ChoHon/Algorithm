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


def fibonacci3(n):
    arr = deque([1, 1])

    for _ in range(n - 2):
        arr.append(arr[1] + arr.popleft())

    return arr[1]


arr = [0] * 91


def fibonacci4(n):

    if n <= 1:
        return n

    if arr[n] != 0:
        return arr[n]

    arr[n] = fibonacci4(n - 1) + fibonacci4(n - 2)
    return arr[n]


print(fibonacci(n))
print(fibonacci2(n))
print(fibonacci3(n))
print(fibonacci4(n))
