# 2025-03-20
# 오전 9:35
# SWEA 5249 최소 신장 트리

import sys
sys.stdin = open('input_5249.txt')

'''
최소 신장 트리:
사이클을 제거하고 모든 노드를 포함, 가중치의 합은 최소
0번부터 V번까지의 노드, E개의 간선을 가진 그래프
'''

# 우선순위 큐(힙)을 사용하여 효율적으로 최소 가중치를 선택
import heapq

# prim 알고리즘
# 최소 스패닝 트리(MST, Minimum Spanning Tree)
def prim(start):
    pq = [(0, start)]  # 노드, 가중치
    MST = [0] * V      # 각 노드가 최소신장트리에 포함되었는지 표시
    min_weight = 0     # 최소신장트리 간선의 가중치를 누적해서 더함

    # 우선순위 큐 (pq, Priority Queue)
    # 가장 작은 가중치를 가진 노드, 그 가중치
    while pq:
        weight, node = heapq.heappop(pq)
        # 만약 최소신장트리에 포함되어 있다면 건너뛰기
        if MST[node]:
            continue
        # if문에서 X, 포함되지 않았다면 트리에 포함시키고 누적합 더하기
        MST[node] = 1
        min_weight += weight

        # 인접 노드 탐색, 힙에 추가
        # 현재 노드와 인접 노드가 연결이 없다면 건너뛰기
        for next in range(V):
            if adj_matrix[node][next] == 0:
                continue
            # 인접 노드가 이미 트리에 포함된 경우에도 건너뛰기
            if MST[next]:
                continue
            # 연결이 있고, 트리에 포함되지 않은 경우 (노드번호, 가중치) 큐에 추가
            heapq.heappush(pq, (adj_matrix[node][next], next))

    # 최소 가중치 반환
    return min_weight

T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

    for num in range(E):
        n1, n2, w = map(int, input().split())
        adj_matrix[n1][n2] = w
        adj_matrix[n2][n1] = w

    print(f'#{t} {prim(0)}')