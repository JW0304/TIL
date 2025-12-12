'''
<입출력>

테스트케이스 T

N, M, R, C, L
지하터널지도 세로, 가로 N, M
맨홀뚜껑 위치 세로, 가로 R, C
탈출 후 소요 시간 L

N x M 지하터널 지도 정보가 주어짐

1 ~ 7 은 해당 위치의 터널 구조물 타입
0 은 터널이 없는 장소

출력은 탈주범이 위치할 수 있는 장소의 개수
'''

'''
<시간 L>

L = 1 일때 맨홀
L = 2 일때 맨홀에서 한칸
L = 3 일때 맨홀에서 두칸
'''

'''
<지하 터널 1 ~ 7>
예외처리가 중요
지하터널은 7종류
0 은 갈 수 없다

갈 수 있는 곳의 최대 수는 총 터널의 개수

1 = 상하좌우
2 = 상하
3 = 좌우
4 = 상우
5 = 하우
6 = 하좌
7 = 상좌
'''

import sys
sys.stdin = open('input_1953.txt')

tunnel = {
    1 : [1, 1, 1, 1],
    2 : [1, 1, 0, 0],
    3 : [0, 0, 1, 1],
    4 : [1, 0, 0, 1],
    5 : [0, 1, 0, 1],
    6 : [0, 1, 1, 0],
    7 : [1, 0, 1, 0],
}

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for t in range(1, T + 1):
    underground_R, underground_C, manhole_R, manhole_C, time_L = map(int, input().split())
    underground = [list(map(int, input().split())) for _ in range(underground_R)]
    visited = [[0] * underground_C for _ in range(underground_R)]
    
    # 스택으로 현재 위치 이동, 이동 가능한 곳들 목록, 다음
    stack = [(manhole_R, manhole_C)]
    visited[manhole_R][manhole_C] = 1
    # 현재 스택과 다음 스택 구분
    next_stack = []
    # 맨홀에 들어갈 때의 시간 1
    time = 1
    
    # 정해놓은 시간이 되기 전까지 스택에 담기
    while time < time_L:
        time += 1

        while stack:
            (temp_r, temp_c) = stack.pop()
            # 현재 위치에 해당되는 숫자
            temp_num = underground[temp_r][temp_c]
            
            # 현재 위치에서 갈 수 있는 곳들
            for i in range(4):
                nr = temp_r + dr[i] * tunnel[temp_num][i]
                nc = temp_c + dc[i] * tunnel[temp_num][i]
                # 조건이 일치하는 경우 건너뛰기 (continue)
                # 조건이 일치하면 멈춤 (break)
                if (temp_r, temp_c) == (nr, nc):
                    continue
                if 0 <= nr < underground_R and 0 <= nc < underground_C:
                    if underground[nr][nc] != 0:
                        adj_num = underground[nr][nc]
                        if visited[nr][nc] == 0:
                            # 현재위치와 목적지의 상하, 좌우가 이어져 있어야 함
                            # 하, 상, 우, 좌 인덱스
                            reverse_d = [1, 0, 3, 2]
                            rr = nr + dr[reverse_d[i]] * tunnel[adj_num][reverse_d[i]]
                            rc = nc + dc[reverse_d[i]] * tunnel[adj_num][reverse_d[i]]
                            # 현재위치 -> 목적지는 가능하므로 목적지 -> 현재위치 가능한지만 확인하면 됨
                            if rr == temp_r and rc == temp_c:
                                next_stack.append((nr, nc))
                                visited[nr][nc] = 1
        
        # 다음 탐색의 스택
        stack = next_stack
        next_stack = []
        # 시간 확인 (탐색 종료 조건)
        if time == time_L:
            break
            
    # if time == time_L:
    #     remain_r, remain_c = stack.pop()
    #     if visited[remain_r][remain_c] != 0:
    #         visited[remain_r][remain_c] = 1
    
    possible_count = 0
    for possible_r in range(underground_R):
        for possible_c in range(underground_C):
            if visited[possible_r][possible_c] == 1:
                possible_count += 1
    
    print(f'#{t} {possible_count}')