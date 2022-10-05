import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

arr = []
while True:
    try:
        arr.append(int(input()))
    except:break

def post_order(s, e):
    if s > e:
        return
    
    d = e + 1
    for i in range(s + 1, e + 1):
        if arr[s] < arr[i]:
            d = i
            break
    
    post_order(s + 1, d - 1)
    post_order(d, e)

    print(arr[s])

    return

post_order(0, len(arr) - 1)
