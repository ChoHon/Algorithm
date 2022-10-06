from heapq import *
import sys

input = sys.stdin.readline

n = int(input())
b_arr = [list(map(int, input().split())) for x in range(n)]


def skyline(b_arr):
    arr, heap, result = [], [], []
    for idx, b in enumerate(b_arr):
        arr.append([b[0], True, idx])
        arr.append([b[2], False, idx])

    arr.sort(key=lambda x: (x[0], -x[1], -b_arr[x[2]][1]))

    for x in arr:
        height = b_arr[x[2]][1]
        end = b_arr[x[2]][2]

        if x[1]:
            if not heap or height > -heap[0][0]:
                result.append([x[0], height])

            heappush(heap, [-height, end])

        else:
            if heap and -heap[0][0] == height:
                heappop(heap)

                while heap and heap[0][1] <= end:
                    pop = heappop(heap)

                if heap:
                    if -heap[0][0] != height:
                        result.append([x[0], -heap[0][0]])
                else:
                    result.append([x[0], 0])

    return result


for i, j in skyline(b_arr):
    print(i, j, end=" ")

"""
3
1 5 5
3 4 6
4 3 7

8
1 11 5
2 6 7
3 13 9
12 7 16
14 3 25
19 18 22
23 13 29
24 4 28

2
1 1 2
1 2 2

4
0 5 5
1 2 7
2 3 5
3 4 5

2
1 1 2
2 1 3
"""
