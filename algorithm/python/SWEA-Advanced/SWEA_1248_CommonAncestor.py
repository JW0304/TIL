# 2025-03-16
# 오전 4:16
# SWEA 1248 공통 조상

import sys
sys.stdin = open('SWEA_Advanced/input_1248.txt')

def common_ancestor(node1, node2):
    global root
    if node1:
        stack1.append(node1)
    if node2:
        stack2.append(node2)
    for i in range(len(stack1)):
        for j in range(len(stack2)):
            if stack1[i] == stack2[j]:
                root = stack1[i]
                return root
    else:
        common_ancestor(parent[node1], parent[node2])

def preorder(node):
    global count
    if node:
        count += 1
        preorder(left[node])
        preorder(right[node])
    return count

T = int(input())
for t in range(1, T + 1):

    V, E, n1, n2 = map(int, input().split())
    pairs = list(map(int, input().split()))

    left = [0] * (V + 1)
    right = [0] * (V + 1)
    parent = [0] * (V + 1)

    for idx in range(E):
        p = pairs[2 * idx]
        c = pairs[2 * idx + 1]

        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

        parent[c] = p

    count = 0
    stack1 = []
    stack2 = []
    common_ancestor(n1, n2)
    print(f'#{t} {root} {preorder(root)}')