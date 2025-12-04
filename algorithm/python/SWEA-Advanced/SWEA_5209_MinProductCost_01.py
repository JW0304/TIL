# 2025-03-18
# 오후 1:02
# SWEA 5209 최소 생산 비용

import sys
sys.stdin = open('input_5209.txt')

'''
Runtime error
10개 중 5개

3 <= N <= 15
'''

import itertools

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    min_num = float('inf')

    # 0부터 N - 1 까지의 인덱스
    numbers = list(range(N))
    # 집합과 길이가 같고 순서가 다른 수열을 구함
    perms = itertools.permutations(numbers)

    subsets = []
    for one_perm in perms:
        subsets.append(list(one_perm))
        
    for p in range(len(subsets)):
        # 현재의 부분집합
        subset = subsets[p]
        
        # 해당하는 행과 열의 값을 더해줌
        temp_num = 0
        for k in range(N):
            temp_num += matrix[k][subset[k]]

        # 최솟값 갱신
        min_num = min(min_num, temp_num)

    print(f'#{t} {min_num}')