'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo
'''

'''
N번의 구슬을 쏴서
W x H 배열의 벽돌을 깨트린다

0 = 빈공간
숫자 = 벽돌

구슬은 좌우로 움직일 수 있고, 항상 맨위에 있는 벽돌만 깨트릴 수 있다
벽돌은 숫자 1 ~ 9, 
구슬이 맞은 벽돌은 상하좌우로 (벽돌의 숫자 - 1) 만큼 같이 제거
즉, 1은 자신만 터짐, 3은 2칸씩 터짐

범위에 있는 벽돌들은 동시에 터진다
터진 후 위에 있는 벽돌들은 아래로 떨어진다

경우의 수를 구한다!!!
N개의 구슬로 최대한 많은 벽돌을 제거한다
남은 벽돌의 수를 출력하라

연산은 팩토리얼이 된다 (제곱인가?)
1. 가로 1 ~ W 에 구슬을 N번 떨어트린다

2. 떨어트렸을 때 범위 내에서 터지는 벽돌들을 모두 계산한다
범위 내의 벽돌들을 모두 지운다

3. 가로 범위 내에서 세로로 계산, 남은 벽돌들을 0이 없으면 아래로 모두 이동한다

4. N번 이후 남은 벽돌의 수를 계산하고, 최소값을 갱신한다.
(++ 남은 블록이 0 인 경우에도 종료한다)

5. 최소값을 출력한다
'''

import sys
sys.stdin = open('input_5656_mini.txt')

from itertools import product

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for t in range(1, T + 1):
    N, W, H = map(int, input().split())
    start_bricks = [list(map(int, input().split())) for _ in range(H)]



    # <경우의 수를 구해야 함>
    # 경우의 수를 구한다!!!
    # 1. 가로 1 ~ W 에 구슬을 N번 떨어트린다

    # ++ N은 1부터 4까지 (수가 작으므로 경우의 수 구할 수 있음)
    # 구슬을 떨어트리는 위치는 [0, 4, 4, 10]과 같이 나올 수 있음
    # N번에 걸쳐 1 ~ W 중에 위치를 구한다



    # <공을 떨어트릴 위치에 대한 조합>
    # 공을 떨어트릴 열의 범위
    # 더 간단히 쓸 수 있었던 것 같은데 기억 안 남
    W_range = []
    for balls in range(W):
        W_range.append(balls)

    # 첫 테스트케이스에서는 210개의 경우의 수
    # 이거 뭔가 아닌 것 같은데...
    # ++ 중복순열로 해야 함
    product_list = list(product(W_range, repeat = N))
    # product_list = itertools.product(W_range, repeat = N)

    # 최소값 미리 설정 (각 경우의 수를 따지기 전에)
    # 출력할 최소값은 W x H 값으로 설정한다 (모든 칸이 블록인 경우를 가정)
    min_num = H * W

    # 각 경우의 수에서 0, 1, 2... N - 1 인덱스 위치에서 공을 떨어트린다
    # 즉, combination_list[cases][drop_order], drop_order 이 0부터 N - 1이다

    pro_len = len(product_list)

    # <각 경우의 수>
    for cases in product_list:

        # 각 경우의 수마다 복사한 상태를 복구한다
        # 리스트 컴프리헨션으로 깊은 복사하기
        try_bricks = [row[:] for row in start_bricks]



        # <떨어트리는 각각의 공>
        for drop_order in range(N):
            # 떨어트릴 현재의 세로 위치 (열의 위치), 가로의 위치는 가장 위
            temp_drop = cases[drop_order]

            # 가로, 세로 중에 가장 위쪽에 있는 블록(가로가 최소)
            # 가로가 0, 1, 2 ... 9 일때 (행의 위치)
            for top_h in range(H):
                # 0 이 아니면 그 블록의 위치를 찾는다 (최상층의 블록)
                if try_bricks[top_h][temp_drop] != 0:
                    top_brick = top_h
                    break

            # 2. 떨어트렸을 때 범위 내에서 터지는 벽돌들을 모두 계산한다
            # 범위 내에 0이 아닌 위치를 모두 구하고 스택에서 빼면서 반복??
            # 이것도 뭔가 아닌 것 같은데...
            
            # 0이 아닌 경우
            # 터지는 블록들은 crash_brick (스택에 넣어놓고 pop하며 지워질 범위를 구함)
            # 없어질 블록들은 erase_brick (없어지지 않음), 한 번에 지우기
            # 그리고 범위 내의 벽돌들을 스택에서 빼면서 모두 지운다
            
            crash_block = [(top_brick, temp_drop)]
            erase_block = [(top_brick, temp_drop)]



            # <부서질 블록>
            while crash_block != []:
                (temp_r, temp_c) = crash_block.pop()

                # 1부터 (블록의 수 - 1)만큼 상하좌우로 깬다
                brick_num = try_bricks[temp_r][temp_c]
                for length in range(1, brick_num):
                    for i in range(4):
                        nr = temp_r + dr[i] * length
                        nc = temp_c + dc[i] * length

                        # 범위 제한
                        if 0 <= nr < H and 0 <= nc < W:

                            # 블록을 깨기 전에 모든 깨지는 범위를 구해야 한다
                            # 부서질 범위의 블록과 없어질 블록들을 모두 구한다
                            if try_bricks[nr][nc] != 0:
                                # 중복을 제외해야 하지 않나....
                                if (nr, nc) not in crash_block:
                                    crash_block.append((nr, nc))
                                if (nr, nc) not in erase_block:
                                    erase_block.append((nr, nc))


            # <지워질 블록>
            # 깰 블록의 범위, 지워질 블록의 범위를 모두 구한 후
            # 블록을 깨고 0으로 만든다
            while erase_block != []:
                (erase_r, erase_c) = erase_block.pop()
                try_bricks[erase_r][erase_c] = 0



        # <아래로 내리기>
        # 모든 블록을 지운 후
        # 3. 각 세로에 대해 가로는 아래에서부터 계산
        # 남은 벽돌들을 0이 없으면 아래로 모두 이동한다

        # 행이 0, 1, 2, ... 9 면 10 - 1, 10 - 2, ... 10 - 10 까지
        for final_c in range(W):
            
            top_zero = 0
            bottom_zero = H - 1
            # 아래에서부터 구한 top_zero과 bottom_zero이 같을 때까지
            # (위에서부터 마지막 0, 아래에서부터 처음 0)
            while top_zero != bottom_zero:

                # 만약 한 열에 대해 위부터 아래까지 0이 없거나 모두 0이면 중지
                zero_list = []
                for zero in range(H):
                    # 0이 하나라도 있으면 중지
                    if try_bricks[zero][final_c] == 0:
                        zero_list.append('0')
                if zero_list == [] or len(zero_list) == H:
                    break

                # 위에서부터 구했을 때 0이 아니면 -1 위치가 top
                for final_1 in range(H):
                    if try_bricks[final_1][final_c] != 0:
                        top_zero = final_1 - 1
                        break

                # 아래에서부터 구했을 때 0이면 bottom
                for final_2 in range(1, H + 1):
                    if try_bricks[H - final_2][final_c] == 0:
                        bottom_zero = H - final_2
                        break

                # bottom 공백 + 1 부터 top 공백 -1 까지
                for middle_range in range(top_zero + 1, bottom_zero):
                    if middle_range + 1 < N:
                        try_bricks[middle_range + 1][final_c] = try_bricks[middle_range][final_c]
                if top_zero != bottom_zero:
                    try_bricks[top_zero + 1][final_c] = 0

        # <경우의 수마다 최솟값을 갱신>
        # 떨어트릴 각각의 공을 모두 떨어트린 후

        # 4. N번 이후 남은 벽돌의 수를 계산하고, 최소값을 갱신한다.
        # (++ 남은 블록이 0 인 경우에도 종료한다)
        remains = 0
        for c in range(W):
            for r in range(H):
                if try_bricks[r][c] != 0:
                    remains += 1

        if remains < min_num:
            min_num = remains

        if remains == 0:
            break

    # 5. 최소값을 출력한다
    print(f'#{t} {min_num}')