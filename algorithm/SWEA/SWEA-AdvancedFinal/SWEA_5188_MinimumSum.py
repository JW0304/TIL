import sys
sys.stdin = open('input_5188.txt')



import heapq

T = int(input())
for t in range(1, T + 1):
    
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    INF = float('inf')
    adj_matrix = [[INF] * N for _ in range(N)]
    adj_matrix[0][0] = matrix[0][0]
    
    # 오른쪽, 아래로 이동
    dr = [1, 0]
    dc = [0, 1]
    
    pq = [(0, 0, matrix[0][0])]
    while pq:
        r, c, w = heapq.heappop(pq)
        
        for i in range(2):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if adj_matrix[nr][nc] > matrix[nr][nc] + matrix[r][c]:
                    adj_matrix[nr][nc] = matrix[nr][nc] + matrix[r][c]
                    heapq.heappush(pq, (nr, nc, adj_matrix[nr][nc]))
    
    print(f'#{t} {adj_matrix[N-1][N-1]}')