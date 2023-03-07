from collections import deque

import sys

read = sys.stdin.readline


def prefix(root):
    if root != ".":
        print(root,end="")
        prefix(tree[root][0])
        prefix(tree[root][1])
        
N = int(read())
tree = dict()
for i in range(N):
    root, left, right = map(str, read().rstrip().split())
    tree[root] = left,right

prefix("A")