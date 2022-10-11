import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for x in range(n)]


def iceberg(arr):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 0

    graph = dict()
    for x in range(n):
        for y in range(m):
            if arr[x][y]:
                linked = []

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny]:
                        linked.append((nx, ny))

                # key : 빙산의 좌표
                # value : 0 - 방산의 높이
                #         1 - 주변 빙산의 좌표 리스트
                #         2 - 순회시 방문 여부
                graph[(x, y)] = [arr[x][y], linked, False]

    # 빙산이 다 없어질 때까지
    while graph:
        for ice in graph.keys():
            graph[ice][2] = False

        # DFS로 빙산들 순회
        que = [list(graph.keys())[0]]
        while que:
            cur_ice = que.pop()

            if graph[cur_ice][2]:
                continue
            graph[cur_ice][2] = True

            for ice in graph[cur_ice][1]:
                que.append(ice)

        # 방문하지 않은 빙산이 있다면(=빙산이 분리되었다면)
        # 걸린 시간을 리턴
        for ice in graph.keys():
            if not graph[ice][2]:
                return cnt

        cnt += 1
        # 주변의 빈칸만큼 빙산 높이 감소
        for ice in graph.keys():
            graph[ice][0] -= 4 - len(graph[ice][1])

        # 빙산 높이가 없어지면 graph에서 삭제
        for ice in list(graph.keys()):
            if graph[ice][0] <= 0:
                for near in graph[ice][1]:
                    graph[near][1].remove(ice)
                del graph[ice]

    return 0


print(iceberg(arr))

"""
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
"""
