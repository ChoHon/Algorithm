# w, h = map(int, input().split())
# arr = [input() for x in w]

w, h = 5, 7
arr = [
    'WLLWWWL',
    'LLLWLLL',
    'LWLWLWW',
    'LWLWLLL',
    'WLLWLWW'
]

land = []
visited = [[False for x in range(h)] for y in range(w)]
for i in range(w):
    for j, lw in enumerate(arr[i]):
        if lw == 'L':
            land.append([i, j])
            visited[i][j] = True

result = 0
def find_treasure(x, y, time):
    global result
    
    if x == -1:
        for i in land:
            find_treasure(i[0], i[1], time)
        
        return

    visited[x][y] = False

    if x < w-1 and visited[x + 1][y]:
        find_treasure(x + 1, y, time + 1)
    
    if x > 0 and visited[x - 1][y]:
        find_treasure(x - 1, y, time + 1)

    if y < h-1 and visited[x][y + 1]:
        find_treasure(x, y + 1, time + 1)

    if y > 0 and visited[x][y - 1]:
        find_treasure(x, y - 1, time + 1)

    result = max(result, time)

find_treasure(-1, 0, 0)
print(result)