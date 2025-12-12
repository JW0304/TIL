import sys
sys.stdin = open('input_5250.txt')

import heapq

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    cost = [[float('inf')] * N for _ in range(N)]
    cost[0][0] = data[0][0]

    pq = [(data[0][0], 0, 0)]

    while pq:
        cur_w, r, c = heapq.heappop(pq)

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            # 범위 확인
            if 0 <= nr < N and 0 <= nc < N:
                # 가려는 값이 더 크면
                if data[nr][nc] > data[r][c]:
                    new_w = cur_w + 1 + (data[nr][nc] - data[r][c])
                else:
                    new_w = cur_w + 1

                # 새로 구한 가중치가 가중치 그래프에서보다 작을 경우
                if new_w < cost[nr][nc]:
                    cost[nr][nc] = new_w
                    heapq.heappush(pq, (new_w, nr, nc))

    print(f'#{t} {cost[N - 1][N - 1]}')