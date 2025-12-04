# 최적화용 input
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

prefix = [[0] * (N + 1) for _ in range(N + 1)]

# 누적합 구하기 (전체 매트릭스)
for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefix[i][j] = (matrix[i - 1][j - 1]
                        + prefix[i - 1][j]
                        + prefix[i][j - 1]
                        - prefix[i - 1][j - 1])

# 구간합 구하기 ((x1, y1) ... (x2, y2))
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    
    result = (prefix[x2][y2]
             - prefix[x1 -1][y2]
             - prefix[x2][y1 - 1]
             + prefix[x1 - 1][y1 - 1])
    
    print(result)
    
'''
브루트포스 시간초과

시간초과 해결:
- readline
- 2차원 누적합
누적합 = 해당 행렬값 + 위쪽 누적합 + 왼쪽 누적합 - 겹친 부분 제외
구간합 = (x2, y2) 누적합 - 위쪽 누적합 - 왼쪽 누적합 + 겹친 부분 복구
'''