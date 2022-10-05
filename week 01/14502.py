# n, m = map(int, input().split())
# arr = []
# for i in range(n):
#     ipt = list(map(int, input().split()))
#     arr.append(ipt)

n, m = 4, 6
arr = [[0, 0, 0, 0, 0, 0], 
    [1, 0, 0, 0, 0, 2],
    [1, 1, 1, 0, 0, 2], 
    [0, 0, 0, 0, 0, 2]]

def infection():
    for i in n:
        for j in m:
            if arr[i][j] == 0:
                if i < n-1 and arr[i+1][j] == 2:
                    arr[i][j] = 2
                
                if i > 0 and arr[i-1][j] == 2:
                    arr[i][j] = 2

                if j < n-1 and arr[i][j+1] == 2:
                    arr[i][j] = 2
                    
                if j > 0 and arr[i][j-1] == 2:
                    arr[i][j] == 2

def lab(k):
    if k == 3:
        pass

    else:
        blank = []
        for i in range(n):
            blank += [[i, j] for j in range(m) if arr[i][j] == 0]

        for i in blank:
            arr[i[0]][i[1]] = 1
            lab(k + 1)
            arr[i[0]][i[1]] = 0
        
            

lab(0)