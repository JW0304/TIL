# 2025-03-14
# 오전 9:12
# SWEA 1861

import sys
sys.stdin = open('input_1861.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result_room = N ** 2
    max_num = 0
    # 모든 칸을 탐색
    for r in range(N):
        for c in range(N):
            count = 1
            stack = [(r, c)]
            start_room = matrix[r][c]
            # 스택이 빌 때까지 (이동할 수 있는 최대 거리)
            while stack:
                (temp_r, temp_c) = stack.pop()
                temp_room = matrix[temp_r][temp_c]
                if temp_room == N **2: continue
                for i in range(4):
                    nr = temp_r + dr[i]
                    nc = temp_c + dc[i]
                    if 0 <= nr < N and 0 <= nc < N:
                        if matrix[nr][nc] == temp_room + 1:
                            count += 1
                            stack.append((nr, nc))
            # 최대값 갱신
            if count > max_num:
                max_num = count
                result_room = start_room
            # 최대값이 같을 경우 숫자가 작은 방
            elif count == max_num and start_room < result_room:
                result_room = start_room

    print(f'#{t} {result_room} {max_num}')

