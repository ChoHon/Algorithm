import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
arr_inorder = list(map(int, input().split()))
arr_postorder = list(map(int, input().split()))
tree = []

def pre_order(s, e):
    if s > e:
        return
    
    root = arr_postorder[e] 
    
    for i in range(len(arr_inorder)):
        if arr_inorder[i] == root:
            d = i
            break
    
    tree.append(root)
    pre_order(s, d)
    pre_order(s + 1, d - 1)

    return

pre_order(0, len(arr_postorder) - 1)