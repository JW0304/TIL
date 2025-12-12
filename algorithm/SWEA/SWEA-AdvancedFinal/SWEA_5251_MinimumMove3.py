import sys
sys.stdin = open('input_5251.txt')

import heapq

T = int(input())
for t in range(1, T + 1):
    N, E = map(int, input().split())
    
    # 인접 리스트
    adj_list = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj_list[s].append((e, w))
        
    # 최단경로 리스트
    INF = float('inf')
    min_dis = [INF] * (N + 1)
    min_dis[0] = 0
    
    # 우선순위 큐 (현재 노드, 가중치)
    pq = [(0, 0)]
    while pq:
        cur_node, cur_w = heapq.heappop(pq)
        # 인접 리스트를 탐색
        for adj_node, adj_w in adj_list[cur_node]:
            next_w = cur_w + adj_w
            if min_dis[adj_node] > next_w:
                min_dis[adj_node] = next_w
                # 최소값 갱신
                heapq.heappush(pq, (adj_node, next_w))
    
    print(f'#{t} {min_dis[N]}')
