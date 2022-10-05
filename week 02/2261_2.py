import sys
import copy
from bisect import *

input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for x in range(n)]


def cal_dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def closest_dots(arr):
    arr.sort(key=lambda x: x[0])
    candidate = sorted([arr[0], arr[1]], key=lambda x: x[1])
    min_dist = cal_dist(arr[0], arr[1])
    start = 0

    for idx, i in enumerate(arr[2:]):
        while start < idx + 2:
            j = arr[start]
            x = i[0] - j[0]
            if x**2 > min_dist:
                candidate.remove(j)
                start += 1
            else:
                break

        # candidate.sort(key=lambda x: x[1])
        dist = int(min_dist**0.5) + 1

        y_arr = [x[1] for x in candidate]
        lower = bisect_left(y_arr, i[1] - dist)
        upper = bisect_right(y_arr, i[1] + dist)

        for j in candidate[lower:upper]:
            min_dist = min(min_dist, cal_dist(i, j))

        if i not in candidate:
            candidate.append(i)
            for k in range(len(candidate) - 2, -1, -1):
                if candidate[k][1] > candidate[k + 1][1]:
                    candidate[k], candidate[k + 1] = candidate[k + 1], candidate[k]
                else:
                    break

    return min_dist


print(closest_dots(arr))
