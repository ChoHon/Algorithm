import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

m, n, l = map(int, input().split())
g_arr = list(map(int, input().split()))
a_arr = [list(map(int, input().split())) for x in range(n)]

def hunter(l, g_arr, a_arr):
    g_arr.sort()
    cnt = 0
    for animal in a_arr:
        pos = bisect_left(g_arr, animal[0])
        if (pos > 0 and pos < m and g_arr[pos] - animal[0] > animal[0] - g_arr[pos - 1]) or pos == m:
            pos -= 1

        if l - g_arr[pos] + animal[0] >= animal[1] and l + g_arr[pos] - animal[0] >= animal[1]:
            cnt += 1

    return cnt

print(hunter(l, g_arr, a_arr))

