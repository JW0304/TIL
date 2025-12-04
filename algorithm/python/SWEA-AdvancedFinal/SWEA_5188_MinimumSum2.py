import sys
sys.stdin = open('input_5188.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    INF = float('inf')
    adj_matrix = [[INF] * N for _ in range(N)]
    adj_matrix[0][0] = matrix[0][0]
    
    dr = [-1, 0]
    dc = [0, -1]
    for r in range(N):
        for c in range(N):
            for i in range(2):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N:
                    if adj_matrix[r][c] > matrix[r][c] + adj_matrix[nr][nc]:
                        adj_matrix[r][c] = matrix[r][c] + adj_matrix[nr][nc]
    
    print(f'#{t} {adj_matrix[N - 1][N - 1]}')