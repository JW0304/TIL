# 2025-03-11
# 오전 11:01
# SWEA 20551 증가하는 사탕 수열

import sys
sys.stdin = open('input_20551.txt')

T = int(input())
for t in range(1, T + 1):
    A, B, C = map(int, input().split())  # 한줄씩 테스트케이스 입력

    # 조건을 만족할 수 없는 경우
    if B == 1 or C <= 2:
        result = -1
        print(f'#{t} {result}')
        continue

    # 이미 조건이 만족되어 있는 경우
    if A < B < C:
        result = 0
        print(f'#{t} {result}')
        continue

    # C -> B, B -> A 순으로 줄여야 함
    count = 0
    if C <= B:
        count += B - (C - 1)
        B = C - 1
    if B <= A:
        count += A - (B - 1)
        A = B - 1
    result = count

    print(f'#{t} {result}')