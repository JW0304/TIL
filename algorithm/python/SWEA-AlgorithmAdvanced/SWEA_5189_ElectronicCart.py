# 2025-03-12
# 오후 3:41
# SWEA 5189 전자카트

import sys
sys.stdin = open('input_5189.txt')

import itertools

T = int(input())
for t in range(1, T + 1):
    N = int(input())

    arr = [[0] + list(map(int, input().split())) for _ in range(N)]
    arr = [[0] * (N + 1)] + arr

    idx = [num for num in range(N)]

    list(itertools.permutations(idx, )


    print(f'#{t} {result}')