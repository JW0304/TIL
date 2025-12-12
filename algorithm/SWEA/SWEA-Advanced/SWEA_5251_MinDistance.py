# 2025-03-20
# 오후 3:10
# SWEA 5251 최소 이동 거리

import sys
sys.stdin = open('input_5251.txt')

# 디익스트라 알고리즘
def dijkstra(start):
    distance[start] = 0

    # 노드의 개수만큼 반복
    for _ in range(N+1):
        min_idx = -1
        min_value = float('inf')

        # 아직 방문하지 않은 노드들 중에서 최단거리에 있는 노드
        for i in range(N+1):
            if not visited[i] and distance[i] < min_value:
                min_idx = i
                min_value = distance[i]
        visited[min_idx] = 1

        # 최단거리 갱신
        for i in range(N+1):
            if adj_matrix[min_idx][i] and not visited[i]:
                distance[i] = min(distance[i], distance[min_idx] + adj_matrix[min_idx][i])

T = int(input())

for t in range(1, T+1):
    N, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    # 인접 행렬 만들기
    adj_matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for s, e, w in edges:
        adj_matrix[s][e] = w
    
    # 방문, 거리 배열 초기화
    visited = [0 for _ in range(N+1)]
    distance = [float('inf') for _ in range(N+1)]

    result = dijkstra(0)
    # 최단 거리 출력
    print(f'#{t} {distance[N]}')
