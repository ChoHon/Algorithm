n = int(input())
arr = [list(map(int, input().split())) for x in range(n)]

def body(arr):
    for i in arr:
        cnt = 0
        for j in arr:
            if i == j:
                continue

            if i[0] < j[0] and i[1] < j[1]:
                cnt += 1

        print(cnt + 1)

body(arr)