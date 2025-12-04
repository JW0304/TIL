import sys
sys.stdin = open('input_5251.txt')

import heapq

T = int(input())
for t in range(1, T + 1):
    N, E = map(int, input().split())
    
    # 인접리스트
    adj_list = [[] for _ in range(N + 1)]
    for i in range(E):
        s, e, w = map(int, input().split())
        adj_list[s].append((e, w))
    
    INF = float('inf')
    min_distance = [INF] * (N + 1)
    min_distance[0] = 0
    
    # (누적 비용, 노드) 순으로 우선순위 큐 초기화
    pq = [(0, 0)]
    while pq:
        cur_w, node = heapq.heappop(pq)
        
        # 이미 더 짧은 경로가 있다면 건너뜁니다.
        if cur_w > min_distance[node]:
            continue
        
        for next_node, edge_w in adj_list[node]:
            new_cost = cur_w + edge_w
            if min_distance[next_node] > new_cost:
                min_distance[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))
                    
    # 최소거리 출력
    print(f'#{t} {min_distance[N]}')
