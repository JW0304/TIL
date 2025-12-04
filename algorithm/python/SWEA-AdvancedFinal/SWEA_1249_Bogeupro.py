import sys
sys.stdin = open('input_1249.txt')

# 최선의 선택
import heapq

# DFS, BFS와 같음
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 가중치를 저장하는 인접행렬 (최소 복구 시간)
    INF = float('inf')
    cost = [[INF] * N for _ in range(N)]
    cost[0][0] = 0

    # 시작점을 큐에 담는다
    # 우선순위 큐: 누적 비용, 행, 열
    # 리스트에 튜플로 넣는다
    queue = [(0, 0, 0)]

    # 큐가 빌 때까지
    while queue:
        w, r, c = heapq.heappop(queue)

        # 최단경로가 가중치보다 더 작은 경우 건너뛰기
        if cost[r][c] < w:
            continue

        # 4방향으로 탐색하는 최단 경로
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            # 범위 확인 후 다음 칸으로 가는 비용
            if 0 <= nr < N and 0 <= nc < N:
                # 다음 칸으로 가는 비용은 현재칸의 가중치 + 다음칸의 값
                new_cost = w + matrix[nr][nc]

                # 다음 칸으로 가는 비용이 최단경로보다 작다면 갱신
                if new_cost < cost[nr][nc]:
                    cost[nr][nc] = new_cost
                    # 다음 칸으로 간다면 그 경로를 큐에 더함
                    heapq.heappush(queue, (new_cost, nr, nc))

    print(f'#{t} {cost[N - 1][N - 1]}')