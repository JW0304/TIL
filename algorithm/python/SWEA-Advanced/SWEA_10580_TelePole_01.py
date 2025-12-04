# 2025-03-11
# 오전 9:29
# SWEA 10580 전봇대

'''
FAIL

전선이 겹치는 경우 Ai <= Bi, Ai >= Bi 에서 두 번 카운트됨
범위를 확실하게 나눌 것!
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
    for i in range(N):
        Ai, Bi = lines[i]
        for j in range(N):
            if lines[j] != (Ai, Bi):
                Aj, Bj = lines[j]

                # 전선이 겹치는 경우 1 (기준선 / or |, 비교선 \)
                if Ai <= Bi:
                    if Ai < Aj and Bi > Bj:
                        count += 1 
                # 전선이 겹치는 경우 2 (기준선 \ or |, 비교선 /)
                if Ai >= Bi:
                    if Ai > Aj and Bi < Bj:
                        count += 1

    # 계산결과 / 2 가 정답
    result = int(count / 2)

    print(f'#{t} {result}')