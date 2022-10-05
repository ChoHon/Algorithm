n = int(input())
l = [list(map(int, input().split())) for y in range(n)]

anw = 1e7
visited = [False] * n

def dfs(o, city, cost):
    global anw

    if o == n:
        if l[city][0]:
            anw = min(anw, cost + l[city][0])

    else:
        for next_city in range(1, n):
            if not visited[next_city] and l[city][next_city]:
                
                visited[next_city] = True                

                dfs(o + 1, next_city, cost + l[city][next_city])

                visited[next_city] = False

dfs(1, 0, 0)
print(anw)