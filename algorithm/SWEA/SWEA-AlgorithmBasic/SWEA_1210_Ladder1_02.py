# 2025-03-02 - 03
# 오후 9:04 - 10:43, 12
# 오전 11:40 - 
# SWEA 1210 Ladder1

import sys
sys.stdin = open('input_1210.txt')

'''
첫째줄에서 마지막줄까지 사다리타기
왼쪽/오른쪽 길이 있으면 옆으로 이동
0 벽, 1 길, 2 도착점

사거리는 존재하지 않음(삼거리만 존재함)
'''

# 아래, 왼쪽, 오른쪽
# ++ 행에서는 아래가 1, 위가 -1임!
dr = [1, 0, 0]
dc = [0, -1, 1]

T = 10
for t in range(1, T + 1):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    
    # 1. 위에서부터 아래로 진행
    # 사다리의 첫번째 줄을 탐색
    for r in range(1):
        for c in range(100):
            
            # 첫번째 줄의 좌표가 1일 경우
            if ladder[r][c] == 1:
                # 현재 위치 지정
                temp_r, temp_c = r, c
                
                # 마지막에 도착할 동안
                while temp_r != 99:
                                
                    # 사다리의 좌표가 1
                    # 오른쪽이 1이면 오른쪽 이동, 아래쪽 한칸 이동
                    if 0 <= temp_c + 1 < 100 and ladder[temp_r][temp_c + 1] == 1:
                        while ladder[temp_r][temp_c + 1] == 1:
                            temp_c += 1
                        temp_r += 1
                    
                    # 왼쪽이 1이면 왼쪽 이동, 아래쪽 한칸 이동
                    elif 0 <= temp_c - 1 < 100 and ladder[temp_r][temp_c - 1] == 1:
                        # 1인 동안 이동
                        while ladder[temp_r][temp_c - 1] == 1:
                            temp_c -= 1
                        temp_r += 1
                    
                    # 아래로 이동
                    else:
                        if 0 <= temp_r < 100:
                            temp_r += 1
                    
                    start = 0
                    if ladder[temp_r][temp_c] == 2:
                        start = c
                        
    # 아래에서 위로 진행 (더 효율적, 다양한 루트를 찾을 필요가 없음)
    # 도착점 2에서 시작
    
    print(f'#{t} {start}')