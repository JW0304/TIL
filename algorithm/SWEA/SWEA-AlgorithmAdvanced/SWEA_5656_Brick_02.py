import sys
sys.stdin = open('input_5656.txt')

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

    # 경우의 수를 구한다
    # 중복순열로 해야 함
    product_list = list(product(W_range, repeat = N))
    # 최소값 미리 설정 (각 경우의 수를 따지기 전에)
    min_num = H * W

    # <각 경우의 수>
    for cases in product_list:
        # 리스트 컴프리헨션으로 깊은 복사하기
        try_bricks = copy.deepcopy(start_bricks)

        # <떨어트리는 각각의 공>
        for drop_order in range(N):
            # 떨어트릴 현재의 세로 위치 (열의 위치), 가로의 위치는 가장 위
            temp_drop = cases[drop_order]
            # 가로, 세로 중에 가장 위쪽에 있는 벽돌(가로가 최소)
            for top_h in range(H):
                if try_bricks[top_h][temp_drop] != 0:
                    top_brick = top_h
                    break
            else:
                break

            # 부서질 벽돌들은 crash_brick (스택에 넣어놓고 pop하며 없어질 범위를 구함)
            # 없어질 벽돌들은 erase_brick (없어지지 않음), 한 번에 지우기
            crash_block = [(top_brick, temp_drop)]
            erase_block = [(top_brick, temp_drop)]

            # <부서질 벽돌>
            while crash_block != []:
                (temp_r, temp_c) = crash_block.pop()
                # 1부터 (벽돌의 수 - 1)만큼 상하좌우로 깬다
                brick_num = try_bricks[temp_r][temp_c]
                for length in range(1, brick_num):
                    for i in range(4):
                        nr = temp_r + dr[i] * length
                        nc = temp_c + dc[i] * length
                        # 범위 제한
                        if 0 <= nr < H and 0 <= nc < W:
                            # 부서질 범위의 벽돌과 없어질 벽돌들을 모두 구한다
                            if try_bricks[nr][nc] != 0:
                                # 중복 제외, stack되는 목록 말고 다른 목록에서 확인
                                if (nr, nc) not in erase_block:
                                    crash_block.append((nr, nc))
                                if (nr, nc) not in erase_block:
                                    erase_block.append((nr, nc))

             # <없어질 벽돌>
            # 없어질 벽돌들을 0으로 만든다
            while erase_block != []:
                (erase_r, erase_c) = erase_block.pop()
                try_bricks[erase_r][erase_c] = 0

            # 벽돌 내리기
            for final_c in range(W):
                # 각 열에 대해 내리기
                non_zero = [try_bricks[r][final_c] for r in range(H) if try_bricks[r][final_c] != 0]
                non_zero = [0] * (H - len(non_zero)) + non_zero
                for r in range(H):
                    try_bricks[r][final_c] = non_zero[r]

            # ++ 들여쓰기
            # <아래로 내리기>
            # 각 세로에 대해 가로 아래에서부터 계산
            # 남은 벽돌들을 0이 없으면 아래로 모두 이동한다
            # for final_c in range(W):
            #     top_zero = -1
            #     bottom_zero = H - 1

            #     while top_zero != bottom_zero:
            #         if top_zero == bottom_zero:
            #             break

            #         # 만약 한 열에 대해 위부터 아래까지 0이 없거나 모두 0이면 중지
            #         zero_list = []
            #         for zero in range(H):
            #             # 0이 하나라도 있으면 중지
            #             if try_bricks[zero][final_c] == 0:
            #                 zero_list.append('0')
            #         if zero_list == [] or len(zero_list) == H:
            #             break

            #         # 위에서부터 구했을 때 0이 아니면 숫자의 -1 위치가 top
            #         for final_1 in range(H):
            #             if try_bricks[final_1][final_c] != 0:
            #                 top_zero = final_1 - 1
            #                 break

            #         # 아래에서부터 구했을 때 0이면 bottom
            #         for final_2 in range(1, H + 1):
            #             if try_bricks[H - final_2][final_c] == 0:
            #                 bottom_zero = H - final_2
            #                 break

            #         # 아래에서부터 올라오며 스왑
            #         for final_r in range(1, H + 1):
            #             if final_r + 1 <= H:
            #                 if try_bricks[- final_r][final_c] == 0 and try_bricks[- final_r - 1][final_c] != 0:
            #                     try_bricks[- final_r][final_c], try_bricks[- final_r - 1][final_c] = try_bricks[- final_r - 1][final_c], try_bricks[- final_r][final_c]

           
        # <경우의 수마다 최솟값을 갱신>
        # 남은 벽돌이 0 인 경우에도 종료
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
