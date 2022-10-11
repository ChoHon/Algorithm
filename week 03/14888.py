import sys

input = sys.stdin.readline

n = int(input())
num_arr = list(map(int, input().split()))
oper_arr = list(map(int, input().split()))

max_result = -1e9
min_result = 1e9


def insert_oper(k, oper_arr, result):
    global max_result, min_result

    if sum(oper_arr) == 0:
        max_result = max(max_result, result)
        min_result = min(min_result, result)

    else:
        if oper_arr[0] > 0:
            oper_arr[0] -= 1
            insert_oper(k + 1, oper_arr, result + num_arr[k + 1])
            oper_arr[0] += 1

        if oper_arr[1] > 0:
            oper_arr[1] -= 1
            insert_oper(k + 1, oper_arr, result - num_arr[k + 1])
            oper_arr[1] += 1

        if oper_arr[2] > 0:
            oper_arr[2] -= 1
            insert_oper(k + 1, oper_arr, result * num_arr[k + 1])
            oper_arr[2] += 1

        if oper_arr[3] > 0:
            oper_arr[3] -= 1
            insert_oper(k + 1, oper_arr, int(result / num_arr[k + 1]))
            oper_arr[3] += 1


insert_oper(0, oper_arr, num_arr[0])
print(max_result, min_result)

"""
2
5 6
0 0 1 0

3
3 4 5
1 0 1 0

6
1 2 3 4 5 6
2 1 1 1
"""
