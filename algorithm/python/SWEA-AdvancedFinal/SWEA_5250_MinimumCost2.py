import sys
sys.stdin = open('input_5250.txt')

import heapq

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    # 인접 행렬
    adj_matrix = [[float('inf')] * N for _ in range(N)]
    adj_matrix[0][0] = 0
    
    # 우선순위 큐, 최소 힙
    # heapq는 리스트를 최소힙처럼 사용할 수 있게 함
    # 가중치, 행, 열
    pq = [(0, 0, 0)]
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    # 최솟값을 선택, 시작은 (0, 0) 위치
    while pq:
        w, r, c = heapq.heappop(pq)
        
        # 사방으로 이동
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            # 범위 내에 있는 경우
            if 0 <= nr < N and 0 <= nc < N:
                # 인접값이 더 큰 경우
                if matrix[nr][nc] > matrix[r][c]:
                    next_w = 1 + adj_matrix[r][c] + (matrix[nr][nc] - matrix[r][c])
                else:
                    next_w = 1 + adj_matrix[r][c]
                
                # 최솟값 갱신한 경우 우선순위 큐에 더하기
                if next_w < adj_matrix[nr][nc]:
                    adj_matrix[nr][nc] = next_w
                    heapq.heappush(pq, (next_w, nr, nc))
    
    print(f'#{t} {adj_matrix[N-1][N-1]}')