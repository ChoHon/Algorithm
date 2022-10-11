import sys

input = sys.stdin.readline

n = int(input())
arr = [input().split() for x in range(n)]
node_dict = {root: [left, right] for root, left, right in arr}


def preorder(root):
    if root == ".":
        return

    print(root, end="")
    preorder(node_dict[root][0])
    preorder(node_dict[root][1])


def inorder(root):
    if root == ".":
        return

    inorder(node_dict[root][0])
    print(root, end="")
    inorder(node_dict[root][1])


def postorder(root):
    if root == ".":
        return

    postorder(node_dict[root][0])
    postorder(node_dict[root][1])
    print(root, end="")


root = "A"
preorder(root)
print("")
inorder(root)
print("")
postorder(root)

"""
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
"""
