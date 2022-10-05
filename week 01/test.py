a = []
c = [0,1,2]
visited = [0 for _ in range(len(c))]
result = []
def permutation(k):
    global visited, result, c
    if k == 0:
        result.append(a[:])
        return
    for i, num in enumerate(c):
        if visited[i] == 0:
            a.append(num)
            visited[i] = 1
            permutation(k-1)
            visited[i] = 0
            a.pop()
    return
permutation(2)
print(result)