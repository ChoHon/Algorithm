n, x = map(int, input().split())
l = list(map(int, input().split()))

def smaller_than_x(x):

    for i in l:
        if i < x:
            print(i)
    
    return

smaller_than_x(x)