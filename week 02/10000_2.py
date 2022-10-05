import sys
from bisect import *

input = sys.stdin.readline
sys.setrecursionlimit(400000)
n = int(input())
a = []
for i in range(n):
    x, r = map(int, input().split())
    a.append((x - r, x + r))
a.sort(key=lambda x: (x[0], -x[1]))
k = 0

# 정렬 기준에 의해서 u는 큰 원, v는 작은 원
def solve(u, v):
    global k
    # 원이 닫히는 부분이 같으면 k++하고 return
    if a[u][1] == a[v][1]:
        k += 1
        return
    # 원이 닫히는 부분이 다르면
    # v의 닫히는 부분에서 열리는 가장 큰 원의 위치 파악
    pos = bisect_left(a, (a[v][1], -2e9))

    # v의 닫히는 부분에서 시작하는 원이 없으면
    if pos == len(a):
        return

    # 그 원이 열리는 점이 v의 닫히는 점과 같다면
    # u, pos로 재귀
    if a[pos][0] == a[v][1]:
        solve(u, pos)


for i in range(n - 1):
    # i번째 원과 i+1번째 원의 시작점이 같으면 solve(i, i+1)
    if a[i][0] == a[i + 1][0]:
        solve(i, i + 1)
print(n + k + 1)
