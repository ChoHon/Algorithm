import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for x in range(n)]


def scheduling_meeting(arr):
    arr.sort(key=lambda x: (x[1], x[0]))
    result = []

    for meeting in arr:
        if not result or result[-1][1] <= meeting[0]:
            result.append(meeting)

    return len(result)


print(scheduling_meeting(arr))

"""
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
"""
