import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())


def josephus(n, k):
    que = deque(range(1, n + 1))
    anw = []

    while que:
        que.rotate(-(k - 1))
        anw.append(que.popleft())

    return anw


string = ""
for i in josephus(n, k):
    string = string + str(i) + ", "
print(f"<{string[:-2]}>")
