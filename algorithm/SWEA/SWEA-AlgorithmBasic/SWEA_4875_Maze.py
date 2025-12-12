'''
# 출발지에서 목적지에 도착하는 경로가 있는지
# 도착 가능하면 1, 아니면 0을 출력한다

# road = 0
# wall = 1
# start = 2
# goal = 3

# import sys
# sys.stdin = open('input_4875.txt')

# T = int(input())
# for t in range(1, T+1):
    
#     # 미로의 크기를 받는다
#     N = int(input())
    
#     # 크기가 NxN인 미로를 만든다
#     maze = [list(map(int, input().strip())) for _ in range(N)]
    
#     # 델타탐색으로 사방으로 이동해야 하나?
#     # 깊이우선탐색으로 도착점까지 갈 수 있는지 본다
#     # 2에서 3까지 가야 한다
#     # 일종의 그래프라고 생각할 수 있다

#     # 시작점에서 주변에 0이 있으면 이동한다
#     # 인접한 0들을 스택에 넣는다(갈 수 있는 곳들)
#     # 간 곳들을 방문표시한다
#     # 하나씩 빼면서 간 곳들을 방문표시한다
#     # 방문했는지 체크하는 걸 빼먹지 않는다!!
    
#     # 스택을 만든다
#     stack = []
    
#     # 방문체크를 만든다
#     a = [0] * N
#     visited = [[0] * N for _ in range(N)]
    
#     # 시작점을 찾아준다
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == 2:
#                 a, b = i, j
#                 start = maze[a][b]
#                 break
    
#     # 가지 않을 곳들
#     for i in range(N):
#         for j in range(N):
#             # 시작점을 방문체크 (어차피 밑에서 방문체크할 것임)
#             # if maze[i][j] == 2:
#             #     visited[i][j] = 1
#             # 벽인 곳을 방문체크 (가지 않음)
#             if maze[i][j] == 1:
#                 visited[i][j] = 1

#     stack.append([a, b])
#     # 델타 탐색
#     r = [-1, 1, 0, 0]
#     c = [0, 0, -1, 1]
    
#     # 초기화
#     nr = 0
#     nc = 0
    
#     # 현재 위치
#     current_location = maze[a][b]
    
#     # 스택이 비지 않을 동안
#     while stack:
#         # 스택에서 꺼낸다
#         current_location = maze[stack[-1][0]][stack[-1][1]]
#         # 방문한 곳을 방문처리한다
#         visited[stack[-1][0]][stack[-1][1]] = 1
        
#         if current_location == 3:
#             result = 1
#             # 3을 찾으면 끝낸다
#             break
#         else:
#             result = 0
        
#         # 방문체크에서 0이면 이동한다
#         # 사방으로만 이동이 가능하다
#         # 상하좌우가 0일 경우
#         # 시작 지점에서 이동해야 한다(그렇지 않으면 모두 1이 나옴)
        
        
#         # 스택의 인접한 곳들을 찾는다
#         for idx_r in range(4):
#             for idx_c in range(4):
#                 # nr과 nc가 N의 범위 내여야 한다
#                 # ++ 값을 지정한 후에
#                 nr = stack[-1][0] + r[idx_r]
#                 nc = stack[-1][1] + c[idx_c]
#                 # ++ 벽인지 확인한다!!
#                 if 0 <= nr < N and 0 <= nc < N:
                
#                 # 방문된 곳인지 체크한다
#                     if visited[nr][nc] == 0:
#                         # 방문되지 않은 곳이면 스택에 더한다 (방문할 수 있는 곳들)
#                         stack.append([nr,nc])
                        
#         # 인접리스트를 찾은 후 스택을 꺼낸다
#         stack.pop()
                              
#     print(f'#{t} {result}')
'''

# SWEA 4875 미로

'''
출발지에서 목적지에 도착하는 경로가 있는지
도착 가능하면 1, 아니면 0을 출력한다
'''
import sys
sys.stdin = open('input_4875.txt')

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
        # ++ 2중 for문을 쓰면 16번이 계산됨
        # ++ 4번만 계산해야 함!!!
        # for sabang in range(4):
        #     ni = ci + di[sabang]
        #     nj = cj + cj[sabang]
        
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