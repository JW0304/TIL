import sys
sys.stdin = open('input_5250.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    # 최소거리를 구하는 행렬
    adj_matrix = [[float('inf')] * N for _ in range(N)]
    adj_matrix[0][0] = 0
    
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    # 최소거리 행렬의 모든 값을 탐색
    for r in range(N):
        for c in range(N):
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                # 범위 설정
                if 0 <= nr < N and 0 <= nc < N:
                    # 인접값이 더 큰 경우
                    if matrix[r][c] < matrix[nr][nc]:
                        val = adj_matrix[r][c] + (matrix[nr][nc] - matrix[r][c]) + 1
                    else:
                        val = adj_matrix[r][c] + 1
                    adj_matrix[r][c] = min(adj_matrix[r][c], val)
    
    # 도착점(N-1, N-1)의 값
    print(f'#{t} {adj_matrix[N-1][N-1]}')