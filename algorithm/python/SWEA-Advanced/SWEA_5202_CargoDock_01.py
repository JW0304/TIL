# 2025-03-13
# 오후 2:06
# SWEA 5202 화물 도크

import sys
sys.stdin = open('input_5202.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())  # 신청서 N개
    
    timetable = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N

    # 끝나는 시간이 가장 짧은 경우
    # s1 ~ e1, s2 ~ e2 일때,
    # e1 <= s2 and e2는 남은 수들 중 가장 작은 수
    # 중복되는 시간표 중 어느 것을 택해도 상관없음

    min_end = timetable[0][1]
    max_end = timetable[0][1]
    count = 0
    # 신청서를 순회하며 s1, e1 선택
    for i in range(N):
        # 가장 작은 종료시간
        if timetable[i][1] <= e1:
            min_end = timetable[i][1]
            start = i
    for j in range(N):
        # 가장 큰 종료시간
        if timetable[j][1] >= e2:
            max_end = timetable[j][1]
    # 첫 신청서 체크
    e1 = min_end
    check[start] = 1
    count += 1

    # 모든 신청서를 체크
    while check != [1] * N:
        for i in range(N):
            s2 = timetable[i][0]
            e2 = timetable[i][1]
            if check[i] == 0:
                # s2는 e1보다 크거나 같아야 함, e2는 가장 작은 값
                if s2 >= e1:
                    if e2 <= max_end:
                        max_end = e2
                if s2 < e1:
                    check[i] = 1
            # 끝점 초기화
            e1 = e2
            e2 = max_end
            count += 1

    print(f'#{t} {count}')