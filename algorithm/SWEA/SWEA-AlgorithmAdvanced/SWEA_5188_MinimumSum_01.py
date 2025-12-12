# 2025-03-12
# 오후 12:19
# SWEA 5188 최소합


import sys
sys.stdin = open('input_5188.txt')

import itertools

T = int(input())
for t in range(1, T + 1):
    N = int(input())

    # 인덱스 0 추가해주면서 matrix 받아오기
    matrix = [[0] + list(map(int, input().split())) for _ in range(N)]
    matrix = [[0] * (N + 1)] + matrix

    # 가로, 세로로 N - 1 만큼 이동
    max_travel = 2 * (N - 1)
    min_num = max_travel * 10  # 이동 거리 * 한 칸의 최댓값
    
    order = [1] * (N - 1) + [0] * (N - 1)
    # 중복을 제외한 경로(순열)
    perm = list(map(list, set(itertools.permutations(order))))

    # 각각의 경로에 대해
    for one_perm in perm:
        # 시작점
        nr, nc = 1, 1
        count = matrix[1][1]  # 시작점의 값
        for move in range(max_travel):
            # dr = [1, 0]이라고 할 때
            # dc = 1 - dr이면 [0, 1]이 되므로
            nr += one_perm[move]
            nc += 1 - one_perm[move]
            # 이동하며 수 더하기
            count += matrix[nr][nc]
            # count가 최솟값을 넘어서면 더 이상 이동할 필요가 없음
            if count >= min_num:
                break
        min_num = min(min_num, count)

    print(f'#{t} {min_num}')