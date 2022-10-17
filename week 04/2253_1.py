import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
check = [[] for x in range(n + 1)]
small = set([int(input()) for x in range(m)])


def solution(n, check, small):
    que = deque([(1, 0, 0)])
    while que:
        v, jump, cnt = que.popleft()
        for temp in [jump + 1, jump, jump - 1]:
            if temp > 0:
                next_v = v + temp
                if next_v == n:
                    return cnt + 1
                if next_v < n and next_v not in small and temp not in check[next_v]:
                    check[next_v].append(temp)
                    que.append((next_v, temp, cnt + 1))
    return -1


print(solution(n, check, small))
