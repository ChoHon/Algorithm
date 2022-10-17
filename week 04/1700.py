import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))


def find_index(arr, n):
    try:
        return arr.index(n)
    except:
        return 101


def schedule_multitap(n, arr):
    cnt = 0
    on_arr = set([])

    for i in range(k):
        next_num = arr[i]

        if len(on_arr) == n and next_num not in on_arr:
            temp_arr = []
            for on_num in on_arr:
                temp_arr.append((find_index(arr[i + 1 :], on_num), on_num))

            off = max(temp_arr)[1]
            on_arr.remove(off)
            cnt += 1

        on_arr.add(next_num)

    return cnt


print(schedule_multitap(n, arr))

"""
4 20
1 2 3 4 5 1 2 3 4 5 1 2 3 4 5 1 2 3 4 5
4

3 14
1 4 3 2 5 4 3 2 5 3 4 2 3 4
4
"""
