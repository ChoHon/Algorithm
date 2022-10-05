import sys

n = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) for x in range(n)]

l.sort()

for i in l:
    print(i)