import sys

input = sys.stdin.readline

n, c = map(int, input().split())
arr = [int(input()) for x in range(n)]


def router(arr, c):
    arr.sort()
    start, end = 1, arr[-1] - arr[0]
    anw = 0

    while start <= end:
        mid = (start + end) // 2

        cnt = 1
        temp = arr[0]
        for i in range(1, len(arr)):
            if temp + mid <= arr[i]:
                cnt += 1
                temp = arr[i]

        if cnt >= c:
            start = mid + 1
            anw = mid

        else:
            end = mid - 1

    return anw


print(router(arr, c))
