import sys
from collections import deque

input = sys.stdin.readline

n = int(input())


def card(n):
    que = deque(range(1, n + 1))

    while len(que) > 1:
        que.popleft()
        que.rotate(-1)

    return que.pop()


print(card(n))
