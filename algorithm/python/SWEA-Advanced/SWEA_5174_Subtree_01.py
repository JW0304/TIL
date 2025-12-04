# 2025-03-15
# 오후 6:06
# SWEA 5174 subtree

import sys
sys.stdin = open('input_5174.txt')

# 서브트리의 노드의 수
def preorder(node):
    global count
    if node:
        count += 1
        preorder(left[node])
        preorder(right[node])
    return count 
        
def inorder(node):
    global count
    if node:
        inorder(left[node])
        count += 1
        inorder(right[node])
    return count
        
def postorder(node):
    global count  # 모든 함수에 매번 global을 해줘야 함
    if node:
        postorder(left[node])
        postorder(right[node])
        count += 1
    return count
        
T = int(input())
for t in range(1, T + 1):
    E, N = map(int, input().split())
    V = E + 1
    pairs = list(map(int, input().split()))
    
    # 부모 정점 번호별로 자식 정점 번호를 저장
    left = [0] * (V + 1)
    right = [0] * (V + 1)
    # 자식 정점 번호별로 부모 정점 번호를 저장
    parent = [0] * (V + 1)
    
    for i in range(E):
        # 부모, 자식 정점은 간선 쌍에서의 짝수, 홀수 인덱스
        p = pairs[2 * i]
        c = pairs[2 * i + 1]
        # 왼쪽, 오른쪽 자식을 차례로 저장
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
        # 부모 저장
        parent[c] = p
    
    root = 0
    # 모든 정점 번호에 대해 부모가 없으면 그 자식은 루트
    for child in range(1, V + 1):
        if parent[child] == 0:
            root = child
    
    count = 0
    print(f'#{t} {postorder(N)}')