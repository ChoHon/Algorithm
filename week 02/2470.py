import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

def solution(arr):
    arr.sort()
    start, end = 0, len(arr) - 1
    temp = 1e10
    anw = []

    while start < end:
        sum_ = arr[start] + arr[end]
        
        if temp > abs(sum_):
            temp = abs(sum_)
            anw = [arr[start], arr[end]]

        if sum_ > 0:
            end -= 1

        elif sum_ < 0:
            start += 1

        else:
            return [arr[start], arr[end]]

    return anw

for i in solution(arr):
    print(i, end=' ')

    

    
