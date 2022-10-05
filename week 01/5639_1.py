import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

arr = []
while True:
    try:
        arr.append(int(input()))
    except:break

tree = []
def make_binary_tree(tree, n):
    if len(tree) == 0:
        tree.append([n, -1, -1])
        return tree
    
    i = 0
    while True:
        if tree[i][0] > n:
            if tree[i][1] == -1:
                tree.append([n, -1, -1])
                tree[i][1] = len(tree) - 1
                break
            else:
                i = tree[i][1]
                continue
        else:
            if tree[i][2] == -1:
                tree.append([n, -1, -1])
                tree[i][2] = len(tree) - 1
                break
            else:
                i = tree[i][2]
                continue

    return tree

def print_binary_tree(tree, node):
    if tree[node][1] > 0:
        print_binary_tree(tree, tree[node][1])

    if tree[node][2] > 0:
        print_binary_tree(tree, tree[node][2])

    print(tree[node][0])
    return

for i in arr:
    make_binary_tree(tree, i)

print_binary_tree(tree, 0)