import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for x in range(n)]


def lan(arr, k):
    arr.sort()
    max_length = 0

    start = 1
    end = sum(arr) // k

    while start <= end:
        mid = (start + end) // 2

        cnt = 0
        for cable in arr:
            cnt += cable // mid

        if cnt >= k:
            start = mid + 1
            max_length = max(max_length, mid)

        else:
            end = mid - 1

    return max_length


print(lan(arr, k))
