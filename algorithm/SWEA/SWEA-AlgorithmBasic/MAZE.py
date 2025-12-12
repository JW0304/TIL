'''
출발지에서 목적지에 도착하는 경로가 있는지
도착 가능하면 1, 아니면 0을 출력한다
'''

# import sys
# sys.stdin = open('input_4875.txt')

T = int(input())
for t in range(1, T+1):
    
    # 미로의 크기를 받는다
    N = int(input())
    
    # 크기가 NxN인 미로를 만든다
    maze = [list(map(int, input().strip())) for _ in range(N)]
    
    # 스택을 만든다
    stack = []
    # 방문체크를 만든다
    visited = [[0] * N for _ in range(N)]
    
    # 시작점을 찾아준다
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                a, b = i, j
                start = maze[a][b]
                break
    
    # 가지 않을 곳들
    for i in range(N):
        for j in range(N):
            # 벽인 곳을 방문체크 (가지 않음)
            if maze[i][j] == 1:
                visited[i][j] = 1
    
    # 델타 탐색
    r = [-1, 1, 0, 0]
    c = [0, 0, -1, 1]
    # 초기화
    nr = 0
    nc = 0
    
    # 스택에 시작점 좌표를 더한다
    stack.append([a, b])
    # 현재 위치
    current_location = maze[a][b]
    
    # 스택이 비지 않을 동안
    while stack:
        # 스택에서 꺼낸다
        current_location = maze[stack[-1][0]][stack[-1][1]]
        # 방문한 곳을 방문처리한다
        visited[stack[-1][0]][stack[-1][1]] = 1
        
        if current_location == 3:
            result = 1
            # 3을 찾으면 끝낸다
            break
        else:
            result = 0
        
        # 스택의 인접한 곳들을 찾는다
        for idx_r in range(4):
            for idx_c in range(4):
                # nr과 nc가 N의 범위 내여야 한다
                # ++ 값을 지정한 후에
                nr = stack[-1][0] + r[idx_r]
                nc = stack[-1][1] + c[idx_c]
                # ++ 미로의 범위 안인지 확인한다!!
                if 0 <= nr < N and 0 <= nc < N:
                
                # 방문된 곳인지 체크한다
                    if visited[nr][nc] == 0:
                        # 방문되지 않은 곳이면 스택에 더한다 (방문할 수 있는 곳들)
                        stack.append([nr,nc])
                        
        # 인접리스트를 찾은 후 스택을 꺼낸다
        stack.pop()
                              
    print(f'#{t} {result}')