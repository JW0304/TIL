# 2025-03-11
# 오전 9:29
# SWEA 10580 전봇대

'''
PASS
'''

import sys
sys.stdin = open('input_10580.txt')

T = int(input())
for t in range(1, T + 1):
    # 전선의 개수
    N = int(input())
    # 전선의 높이
    lines = []
    for _ in range(N):
        A, B = map(int, input().split())
        lines.append((A, B))

    count = 0
    # 기준이 되는 전선, 비교할 전선
    for Ai, Bi in lines:
        for Aj, Bj in lines:
            if (Aj, Bj) != (Ai, Bi):
                # 전선이 겹치는 경우 1 (기준선 / or |, 비교선 \)
                if Ai < Aj and Bi > Bj:
                        count += 1 
                # 전선이 겹치는 경우 2 (기준선 \ or |, 비교선 /)
                elif Ai > Aj and Bi < Bj:
                        count += 1

    # 계산결과 / 2 가 정답
    result = int(count / 2)

    print(f'#{t} {result}')