import sys

input = sys.stdin.readline

string = input().strip()
n = len(string)

sa = [x for x in range(n)]
group = [0] * (n + 1)
new_group = [0] * (n + 1)

for i in range(n):
    group[i] = ord(string[i])

group[n] = -1
new_group[n] = -1
t = 1

while t < n:
    sa.sort(key=lambda x: (group[x], group[min(x + t, n)]))

    for i in range(1, n):
        p, q = sa[i - 1], sa[i]
        if group[p] != group[q] or group[min(p + t, n)] != group[min(q + t, n)]:
            new_group[q] = new_group[p] + 1
        else:
            new_group[q] = new_group[p]

    if new_group[n - 1] == n - 1:
        break

    t *= 2
    group = new_group[:]

print(sa)
print(group)

LCP = [0] * n
length = 0
for i in range(n):
    k = group[i]
    if k == 0:
        continue

    p = sa[k - 1]

    while (
        i + length < n and p + length < n and string[i + length] == string[p + length]
    ):
        length += 1

    LCP[k] = length

    if length:
        length -= 1

max_LCP = 0
idx = 0
