from collections import deque

n = int(input())

def check(n, arr):
    new_arr = []
    for i in range(1, n+1):
        if i not in arr:
            for j in range(1, len(arr) + 1):
                if abs(arr[len(arr) - j] - i) == j:
                    break
                else:
                    new_arr.append(arr + [i])
    return new_arr

def solution(n):
    anw = 0
    queue = deque([[x] for x in range(1, n + 1)])
    while queue:
        arr = deque.popleft(queue)
        
        if len(arr) == n:
            anw += 1
        else:
            if check(n, arr):
                queue.extend(check(n, arr))
    
    return anw

print(solution(n))