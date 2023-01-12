# https://school.programmers.co.kr/learn/courses/30/lessons/77485

from collections import deque

def solution(rows, columns, queries):
    arr = [[x + y*columns for x in range(1, columns + 1)] for y in range(rows)]

    result = []
    for query in queries:
        top_r, left_c, bottom_r, right_c = query
        arr_r = deque()
        
        
        for c in range(left_c - 1, right_c):
            arr_r.append(arr[top_r - 1][c])

        for r in range(top_r, bottom_r):
            arr_r.append(arr[r][right_c - 1])

        for c in range(right_c - 2, left_c - 2, -1):
            arr_r.append(arr[bottom_r - 1][c])

        for r in range(bottom_r - 2, top_r - 1, -1):
            arr_r.append(arr[r][left_c - 1])
        
        result.append(min(arr_r))
        
        arr_r.rotate()
        
        i = 0
        for c in range(left_c - 1, right_c):
            arr[top_r - 1][c] = arr_r[i]
            i += 1

        for r in range(top_r, bottom_r):
            arr[r][right_c - 1] = arr_r[i]
            i += 1

        for c in range(right_c - 2, left_c - 2, -1):
            arr[bottom_r - 1][c] = arr_r[i]
            i += 1

        for r in range(bottom_r - 2, top_r - 1, -1):
            arr[r][left_c - 1] = arr_r[i]
            i += 1
                        
    return result