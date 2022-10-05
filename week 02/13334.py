from heapq import *
import sys

input = sys.stdin.readline

n = int(input())
arr = [sorted(list(map(int, input().split()))) for x in range(n)]
d = int(input())

# Line Sweep
def rail(arr, d):
    result = 0
    heap = []
    # 사무실 위치를 기준으로 오름차순 정렬
    arr.sort(key=lambda x: x[1])

    for start, end in arr:
        limit = end - d

        if start >= limit:
            heappush(heap, start)

        # heap의 root가 철로 안의 집을 가리킬 때까지 pop
        while heap and heap[0] < limit:
            heappop(heap)

        result = max(result, len(heap))

    return result


print(rail(arr, d))
