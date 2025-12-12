# 2025-03-04
# 오후 3:19
# SWEA 1226. 미로1

import sys
sys.stdin = open('input_1226_mini.txt')


T = 1
N = 4
ROAD = 0
WALL = 1
START = 2
GOAL = 3

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

result = 0

for t in range(1, T + 1):
    tc = input()
    maze = [list(map(int, input().strip())) for _ in range(N)]

    # 시작점 찾기
    for r in range(N):
        for c in range(N):
            if maze[r][c] == START:
                temp_r = r
                temp_c = c


    # 스택 만들기
    stack = [(temp_r, temp_c)]
    # 방문 체크
    visited = [[0] * N for _ in range(N)]

    # ++ 스택이 빌 때까지 (도착점에 못 갈수도 있음)
    while stack:
        temp_r, temp_c = stack.pop()
        print(temp_r,temp_c)
        # 방문했을 때 방문체크
        visited[temp_r][temp_c] = 1

        # 네 가지 방향을 탐색
        for i in range(4):
            nr = temp_r + dr[i]
            nc = temp_c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if maze[nr][nc] == GOAL:
                    result = 1
                    break

                if maze[nr][nc] == ROAD:
                    # 방문체크하고 스택에 담기 (갈 수 있는 곳들, 브랜치)
                    if visited[nr][nc] == 0:
                        # ++ 방문체크
                        visited[nr][nc] = 1
                        stack.append((nr, nc))

        # if maze[temp_r][temp_c] != GOAL:
        #     result = 0
        # else:
        #     result = 1

    print(f'#{t} {result}')