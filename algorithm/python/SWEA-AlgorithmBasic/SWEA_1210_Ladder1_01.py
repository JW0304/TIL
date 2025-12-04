# SWEA
# 1210. Ladder1
# 2025-02-17 월
# 오후 4:14-8:21

import sys
sys.stdin = open('input_ladder.txt')

'''
X 표시에 도착하게 되는 출발점 인덱스의 번호는?
사다리는 1, 빈 곳은 0, 도착 지점은 2로 표현된다.
100 x 100 크기의 2차원 배열
'''

# 상, 좌, 우
dr = [-1, 0, 0]
dc = [0, -1, 1]

T = 10
for t in range(1, T+1):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    '''
    ladder[0]의 행 중에 1인 경우 아래로 내려가기
    또는 ladder[99]의 행 중에 2인 경우 위로 올라가기
    사거리(사방으로 1이 존재하는 경우)는 존재하지 않음
    삼거리(세 방향으로 1이 존재하는 경우)는 가로로 이동 -> 세로로 이동
    
    방향 이동을 어떻게 해야?
    델타 이동: 상, 좌, 우
    
    조건 설정: 
    if 좌 또는 우에 1이 있는지 확인, 1이 있으면 옆으로 이동
    else 위로 이동
    '''

    # ladder[99]에서 시작해서 ladder[0]으로 올라가기
    for x in range(100):
        if ladder[99][x] == 2:
            start = x
            break

    # 시작 위치
    r, c = 99, start

    while r > 0:  # 0에 도달하면 끝
        # 좌측 이동
        if c-1 >= 0 and ladder[r][c-1] == 1:
            while c-1 >= 0 and ladder[r][c-1] == 1:
                c -= 1
            r -= 1
        # 우측 이동
        elif c+1 < 100 and ladder[r][c+1] == 1:
            while c+1 < 100 and ladder[r][c+1] == 1:
                c += 1
            r -= 1
        else:
            r -= 1

    # 최종 도착지 (r == 0)
    print(f'#{t} {c}')