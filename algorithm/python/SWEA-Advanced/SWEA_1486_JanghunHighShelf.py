# 2025-03-14
# 오전 10:24
# SWEA 1486

import sys
sys.stdin = open('input_1486.txt')

T = int(input())
for t in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    result_height = sum(arr)
    subset_count = 2 ** N  
    # N = 20일때 최대 1,048,576
    # 비트마스크 기법은 N이 최대 20 ~ 30일때 효율적
    for i in range(subset_count):
        subset = []
        for j in range(N):
            if i & (1 << j):
                subset.append(arr[j])
        temp_height = sum(subset)
        if B <= temp_height < result_height:
            result_height = temp_height

    print(f'#{t} {result_height - B}')