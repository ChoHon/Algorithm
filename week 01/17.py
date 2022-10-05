def make_new_str(n, s):
    new_str = ''

    for c in s:
        cc = c * n
        new_str += cc

    return new_str

t = int(input())
for i in range(t):
    n, s = input().split()
    print(make_new_str(int(n), s))