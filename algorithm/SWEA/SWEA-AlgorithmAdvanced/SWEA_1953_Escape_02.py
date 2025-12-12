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
    
    # 스택으로 탈주범의 현재의 이동 위치, 다음의 이동 위치
    stack = [(manhole_R, manhole_C)]
    next_stack = []
    # 탈주범이 위치 가능한 장소, 맨홀에 들어갈 때의 시간
    possible = set()
    time = 1
    
    # 시간이 다할 때까지 탐색
    # 시간 + 1 -> 현재 스택의 사방을 탐색, 방문 체크 -> 다음 스택을 현재 스택으로, 초기화 -> 시간 확인
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
                if (temp_r, temp_c) == (nr, nc):
                    continue
                if 0 <= nr < underground_R and 0 <= nc < underground_C:
                    if underground[nr][nc] != 0:
                        adj_num = underground[nr][nc]
                        if (nr, nc) not in possible:
                            # 현재위치와 목적지의 상하, 좌우가 이어져 있어야 함
                            # 하, 상, 우, 좌 (인덱스)
                            reverse_d = [1, 0, 3, 2]
                            rr = nr + dr[reverse_d[i]] * tunnel[adj_num][reverse_d[i]]
                            rc = nc + dc[reverse_d[i]] * tunnel[adj_num][reverse_d[i]]
                            # 현재위치 -> 목적지는 가능하므로 목적지 -> 현재위치 가능한지만 확인하면 됨
                            if rr == temp_r and rc == temp_c:
                                next_stack.append((nr, nc))
                                possible.add((nr, nc))
        
        # 다음 탐색의 스택
        stack = next_stack
        next_stack = []
        # 시간 확인 (탐색 종료 조건)
        if time == time_L:
            break
        
    result = len(possible)
    # 시간이 1일 경우
    if time_L == 1:
        result = 1
    
    print(f'#{t} {result}')