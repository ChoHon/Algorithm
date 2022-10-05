import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for x in range(n)]

def hots(arr, k):
    arr.sort()
    start, end = arr[0], arr[0] + k
    temp = 0

    while start <= end:
        mid = (start + end) // 2

        dist_arr = [mid - x for x in arr if mid > x]
        
        if sum(dist_arr) < k:
            temp = mid
            start = mid + 1

        elif sum(dist_arr) > k:
            end = mid - 1

        else:
            return mid

    return temp

print(hots(arr, k))