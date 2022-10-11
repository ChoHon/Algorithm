import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

k = int(input())
arr = []
for _ in range(k):
    v, e = map(int, input().split())
    temp = [list(map(int, input().split())) for x in range(e)]
    arr.append([[v, e]] + temp)


def dfs_recursion(graph, start, color):
    global is_bipartite

    visited[start] = True

    # v가 색칠된 적 없으면 색칠
    if colored[start] == -1:
        colored[start] = color

    for next_v in graph[start]:
        # 다음 v의 색이 지금 v의 색과 같으면
        # 이분 그래프가 아님
        if colored[next_v] == color:
            is_bipartite = False

        if not visited[next_v]:
            # 탐색하면서 색을 번갈아가면서 색칠
            dfs_recursion(graph, next_v, (not color))

    return


for temp in arr:
    v, e = temp[0]
    graph = [[] for x in range(v + 1)]
    for v1, v2 in temp[1:]:
        graph[v1].append(v2)
        graph[v2].append(v1)

    visited = [False] * (v + 1)
    colored = [-1] * (v + 1)
    is_bipartite = True

    for i in range(v + 1):
        if not visited[i]:
            dfs_recursion(graph, i, True)

    if is_bipartite:
        print("YES")
    else:
        print("NO")
