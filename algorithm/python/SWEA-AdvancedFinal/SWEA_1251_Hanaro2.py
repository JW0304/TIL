import sys
sys.stdin = open('input_1251.txt')

import heapq

T = int(input())
for t in range(1, T + 1):
    N = int(input())  # 섬의 개수 입력
    x_list = list(map(int, input().split()))  # 각 섬의 x 좌표
    y_list = list(map(int, input().split()))  # 각 섬의 y 좌표
    E = float(input())  # 환경 부담 세율

    visited = [0] * N
    pq = [(0, 0)] # 비용, 섬의 번호

    mst_cost = 0

    while pq:
        # 현재의 위치와 비용
        cost, island = heapq.heappop(pq)

        # 이미 방문한 섬이라면 건너뛰기
        if visited[island]:
            continue

        visited[island] = 1
        mst_cost += cost

        # 현재 섬에서 갈 수 있는 섬들
        for i in range(N):
            if not visited[i]:
                cost_i = ((x_list[island] - x_list[i]) ** 2 +
                          (y_list[island] - y_list[i]) ** 2) * E
                # 갈 수 있는 섬을 가는 비용과 섬을 더함
                heapq.heappush(pq, (cost_i, i))

    # 최종 비용을 반올림하여 출력
    print(f'#{t} {round(mst_cost)}')