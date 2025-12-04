# 2025-03-15
# 오후 9:00
# SWEA 5178

import sys
sys.stdin = open('input_5178.txt')

def sum_of_nodes(list):
    for j in range(N, 1, -1):
        list[j//2] += list[j]

T = int(input())  # 테스트 케이스 개수 입력
for t in range(1, T + 1):
    # 총 노드 개수 N, 리프 노드 개수 M, 값을 출력할 노드 번호 L
    N, M, L = map(int, input().split())
    # leafs = [list(map(int, input().split())) for _ in range(M)]
    
    tree_value = [0] * (N + 1)
    # for i in range(len(leafs)):
    #     value[leafs[i][0]] = leafs[i][1]
    
    # 값은 아래처럼 받을 수도 있음
    for _ in range(M):
        # 리프 노드의 번호, 저장값
        num, node_value = map(int, input().split())  
        tree_value[num] = node_value
    
    # 리프 노드를 제외한 나머지 노드에는 자식 노드의 합
    # value를 역순으로 1까지 순회, i // 2(부모 노드)에 값을 더하기
    sum_of_nodes(tree_value)
    
    print(f'#{t} {tree_value[L]}')