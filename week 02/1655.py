from heapq import *
import sys

input = sys.stdin.readline

n = int(input())


def speak_mid(n):
    max_heap = []
    min_heap = []

    for _ in range(n):
        ipt = int(input())

        # 총 원소가 짝수일 때 작은 쪽을 선택해야해서 max_heap의 root가 중간값
        # 새로 들어온 값을 현재 중간값과 비교해서 힙트리에 삽입
        if not max_heap:
            heappush(max_heap, -ipt)

        elif -max_heap[0] >= ipt:
            heappush(max_heap, -ipt)

        elif -max_heap[0] < ipt:
            heappush(min_heap, ipt)

        # max_heap은 min_heap보다 크기가 같거나(총 원소가 짝수) 1개 더 많아야한다(총 원소가 홀수)
        if len(max_heap) < len(min_heap):
            heappush(max_heap, -heapq.heappop(min_heap))

        elif len(max_heap) > len(min_heap) + 1:
            heappush(min_heap, -heapq.heappop(max_heap))

        print(-max_heap[0])


speak_mid(n)
