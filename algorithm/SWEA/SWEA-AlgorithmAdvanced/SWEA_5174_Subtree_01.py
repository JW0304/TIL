# 2025-03-11
# 오후 8:33
# SWEA 5174 subtree
    
def pre_order(node):
    global count
    if node:
        count += 1  # 할일 처리
        pre_order(left[node])
        pre_order(right[node])
        
# def in_order(node):
#     if node:
#         in_order(left[node])
#         count += 1
#         in_order(right[node])
        
# def post_order(node):
#     if node:
#         post_order(left[node])
#         post_order(right[node])
#         count += 1

import sys
sys.stdin = open('input_5174.txt')

T = int(input())
for t in range(1, T + 1):
    # 총 노드의 수는 E + 1
    # 간선의 개수 E, 루트 노드 N
    
    # 노드 N을 루트로 하는 서브 트리에 속한 노드의 수
    # 즉, 노드 N부터 순회를 했을 때 순회한 수
    E, N = map(int, input().split())
    node_pairs = list(input().split())
    
    left = [0] * (E + 1)
    right = [0] * (E + 1)
    par = [0] * (E + 1)
    
    # 간선의 개수만큼 쌍이 있다
    for i in range(E):
        p, c = node_pairs[2*i], node_pairs[2*i+1]
        # 자식을 인덱스로 부모를 저장 (루트를 찾을 때)
        par[c] = p
        
        # 부모 노드를 인덱스로 자식 리스트를 만든다
        # 왼쪽 자식 -> 오른쪽 자식
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
            
    # 루트 찾기
    root = 1
    for i in range(1, N + 1):
        if par[i] == 0:
            root = i
            break
    
    # 카운트 정의
    count = 0
    result = pre_order(N)
    
    print(f'#{t} {result}')
    
