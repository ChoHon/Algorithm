import sys

input = sys.stdin.readline

n = int(input())
arr = list((map(int, input().split())))
m = int(input())
ipt = list(map(int, input().split()))


def search(arr, n):
    start, end = 0, len(arr)

    while end > start:
        mid = (start + end) // 2

        if arr[mid] == n:
            return 1

        elif arr[mid] > n:
            end = mid

        else:
            start = mid + 1

    return 0


for i in ipt:
    print(search(arr, i))
