import sys

input = sys.stdin.readline


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


n = int(input())
arr = [input().strip().split() for x in range(n)]
arr = [Node(value, left, right) for value, left, right in arr]

node_dict = {}
for i in range(n):
    node_dict[arr[i].value] = i

root = arr[0]


def preorder(root):

    print(root.value, end="")
    if root.left != ".":
        preorder(arr[node_dict[root.left]])
    if root.right != ".":
        preorder(arr[node_dict[root.right]])


def inorder(root):

    if root.left != ".":
        inorder(arr[node_dict[root.left]])
    print(root.value, end="")
    if root.right != ".":
        inorder(arr[node_dict[root.right]])


def postorder(root):

    if root.left != ".":
        postorder(arr[node_dict[root.left]])
    if root.right != ".":
        postorder(arr[node_dict[root.right]])
    print(root.value, end="")


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
