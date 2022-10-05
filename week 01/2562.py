l = [int(input()) for x in range(9)]

def find_max(l):    
    mx = 0
    idx = 1
    
    for i in range(9):
        if l[i] > mx:
            mx = l[i]
            idx = i+1

    return mx, idx

mx, idx = find_max(l)
print(mx, idx)