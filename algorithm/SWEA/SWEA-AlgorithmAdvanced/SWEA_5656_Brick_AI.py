# import sys
# sys.stdin = open('input_5656.txt')
# from pprint import pprint
from itertools import product
import copy

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for t in range(1, T + 1):
    N, W, H = map(int, input().split())
    start_bricks = [list(map(int, input().split())) for _ in range(H)]

    # 공을 떨어트릴 열의 범위
    W_range = []
    for balls in range(W):
        W_range.append(balls)

    # 중복순열로 해야 함
    product_list = list(product(W_range, repeat = N))
    min_num = H * W

    # <각 경우의 수>
    for cases in product_list:
        try_bricks = copy.deepcopy(start_bricks)

        # <떨어트리는 각각의 공>
        for drop_order in range(N):
            temp_drop = cases[drop_order]
            for top_h in range(H):
                if try_bricks[top_h][temp_drop] != 0:
                    top_brick = top_h
                    break
            else:
                break

            # 부서질 벽돌: crash_brick (스택에 넣어놓고 pop하며 없어질 범위를 구함)
            # 없어질 벽돌: erase_brick (없어지지 않음), 한 번에 지우기
            crash_block = [(top_brick, temp_drop)]
            erase_block = [(top_brick, temp_drop)]

            # <부서질 벽돌> 1부터 (벽돌의 수 - 1)만큼 상하좌우로 깬다
            while crash_block != []:
                (temp_r, temp_c) = crash_block.pop()
                brick_num = try_bricks[temp_r][temp_c]
                for length in range(1, brick_num):
                    for i in range(4):
                        nr = temp_r + dr[i] * length
                        nc = temp_c + dc[i] * length
                        if 0 <= nr < H and 0 <= nc < W:
                            if try_bricks[nr][nc] != 0:
                                if (nr, nc) not in erase_block:
                                    crash_block.append((nr, nc))
                                if (nr, nc) not in erase_block:
                                    erase_block.append((nr, nc))

             # <없어질 벽돌> 없어질 벽돌들을 0으로 만든다
            while erase_block != []:
                (erase_r, erase_c) = erase_block.pop()
                try_bricks[erase_r][erase_c] = 0

            # <벽돌 내리기> 각 열에서 0이 아닌 갯수를 구해서 열을 대체함
            for final_c in range(W):
                non_zero = [try_bricks[r][final_c] for r in range(H) if try_bricks[r][final_c] != 0]
                non_zero = [0] * (H - len(non_zero)) + non_zero
                for r in range(H):
                    try_bricks[r][final_c] = non_zero[r]

        # <경우의 수마다 최솟값을 갱신> 남은 벽돌이 0 인 경우에도 종료
        remains = 0
        for c in range(W):
            for r in range(H):
                if try_bricks[r][c] != 0:
                    remains += 1
        if remains < min_num:
            min_num = remains
        if remains == 0:
            break

    # 최소값을 출력
    print(f'#{t} {min_num}')