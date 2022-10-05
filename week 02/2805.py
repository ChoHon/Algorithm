import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

def cut_tree(arr, m):
    arr.sort()
    start, end = 1, arr[-1]
    temp = 0

    while start <= end:
        mid = (start + end) // 2

        cut_length = sum([x - mid for x in arr if x > mid])

        if cut_length == m:
            return mid

        elif cut_length < m:
            end = mid - 1

        else:
            temp = mid            
            start = mid + 1

    return temp

print(cut_tree(arr, m))