from heapq import *
import sys

input = sys.stdin.readline

n = int(input())


def max_heap(n):
    heap = []

    for i in range(n):
        ipt = int(input())

        if ipt == 0:
            if heap:
                print(-heappop(heap))
            else:
                print(0)

        else:
            heappush(heap, -ipt)

    return


max_heap(n)
