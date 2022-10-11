import sys

input = sys.stdin.readline

k = int(input())
arr = []
for _ in range(k):
    v, e = map(int, input().split())
    temp = [list(map(int, input().split())) for x in range(e)]
    arr.append([[v, e]] + temp)


def bipartite(arr):
    for temp in arr:
        v, e = temp[0]
        graph = [[] for x in range(v + 1)]
        for v1, v2 in temp[1:]:
            graph[v1].append(v2)
            graph[v2].append(v1)

        visited = [False] * (v + 1)
        colored = [-1] * (v + 1)
        is_bipartite = True

        def dfs_stack(graph, start):
            que = [[start, True]]

            while que:
                cur_v, color = que.pop()

                visited[cur_v] = True

                # v가 색칠된 적 없으면 색칠
                if colored[cur_v] == -1:
                    colored[cur_v] = color

                for next_v in graph[cur_v]:
                    # 다음 v의 색이 지금 v의 색과 같으면
                    # 이분 그래프가 아님
                    if colored[next_v] == color:
                        return False

                    if not visited[next_v]:
                        # 탐색하면서 색을 번갈아가면서 색칠
                        que.append([next_v, not color])

            return True

        for i in range(v + 1):
            if not visited[i] and not dfs_stack(graph, i):
                is_bipartite = False

        if is_bipartite:
            print("YES")
        else:
            print("NO")


bipartite(arr)


"""
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2

1
5 4
1 2
1 3
2 4
3 5
"""
