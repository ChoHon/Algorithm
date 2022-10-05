def find_longest(m, l):
    l.sort()
    max_d = m - l[-1]

    i = 1
    while i < len(l):
        if (l[i] - l[i-1]) > max_d:
            max_d = l[i] - l[i-1]
        
        i += 1

    return max_d

def find_big_sq(w, h, l):
    w_l = [0]
    h_l = [0]
    
    for d, n in l:
        if d == 1:
            w_l.append(n)
        else:
            h_l.append(n)

    max_w = find_longest(w, w_l)
    max_h = find_longest(h, h_l)

    return max_w * max_h

w, h = map(int, input().split())
t = int(input())
l = [list(map(int, input().split())) for x in range(t)]

print(find_big_sq(w, h, l))