import sys
input = sys.stdin.readline

n, b = map(int, input().split())
arr = [list(map(int, input().split())) for x in range(n)]

def cal_remain(arr, m):
    for i in range(n):
        for j in range(n):
            arr[i][j] %= m

    return arr

def matrix_mul(arr_a, arr_b):
    temp = [[0] * n for x in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp[i][k] += arr_a[i][j] * arr_b[j][k]

    return temp

def matrix_ex_mul(arr, b):
    if b == 1:
        return cal_remain(arr, 1000)
    
    elif b % 2 == 0:
        temp = matrix_ex_mul(arr, b//2)
        return cal_remain(matrix_mul(temp, temp), 1000) 
    
    else:
        temp = matrix_ex_mul(arr, b-1)
        return cal_remain(matrix_mul(temp, arr), 1000)

arr = matrix_ex_mul(arr, b)

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print('')