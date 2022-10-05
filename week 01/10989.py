import sys

sort_l = [0] * 10001
for n in range(int(sys.stdin.readline())):
    sort_l[int(sys.stdin.readline())] += 1

for l in range(len(sort_l)):
    if sort_l[l] != 0:
        t = sort_l[l]
        for i in range(t):
            print(l)