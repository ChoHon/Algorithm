n = int(input())

def gugudan(n):
    for i in range(1, 10):
        print('{} * {} = {}'.format(n, i, n*i))
    
    return

gugudan(n)