import sys
input = sys.stdin.readline

import heapq
from collections import deque

def knight(board, W, H, w, h, dw, dh):
    # print("---def knight start---")
    global now, prefix, result
    
    # K의 횟수만큼 나이트로 이동 가능
    for ki in range(1, K + 1):
        
        # 갱신
        next = deque()
        
        # print("ki:", ki)
        
        # 현재 턴에서 나이트로 이동 가능한 지점들
        while len(now) != 0:
            w, h = now.popleft()
            
            # print("w, h:", w, h)
            
            # 도착한 경우, 결과에 이동횟수 추가
            if (w, h) == (H-1, W-1):
                result.append(prefix[h][w] - 1) # 여기도 가로세로 잘못 적음, 왜 -1?
                return
            
            # 나이트 이동: 상하+좌우, 좌우+상하 방향
            for i in range(4):
                kh = h + dh[i]
                kw_l = w - dw[i]
                kw_r = w + dw[i]
                    
                # 장애물이 아니고 미방문이면 ki 더하기
                if 0 <= kh < H and 0 <= kw_l < W:
                    if board[kh][kw_l] != 1 and prefix[kh][kw_l] == 0:
                        prefix[kh][kw_l] += ki
                        next.append((kh, kw_l))
                        # 도착한 값이면 result에 추가
                        if (kh, kw_l) == (H-1, W-1):
                            result.append(prefix[kh][kw_l])
                
                if 0 <= kh < H and 0 <= kw_r < W:
                    if board[kh][kw_r] != 1 and prefix[kh][kw_r] == 0:
                        prefix[kh][kw_r] += ki
                        next.append((kh, kw_r))
                        # 도착한 값이면 result에 추가
                        if (kh, kw_r) == (H-1, W-1):
                            result.append(prefix[kh][kw_r])
                        
            # print("prefix:", prefix)
            # print("next:", next)
                        
        # 다음 턴으로 이동
        now = next
                
        # print("result:", result)
        # print("now:", now)
        
    return result, now

def pawn(board, W, H, w, h, dw2, dh2):
    # print()
    # print("---def pawn start---")
    global now, prefix, result
    
    # 현재 턴에서 폰으로 이동 가능한 지점들    
    while now != []:
        w, h = now.pop(0)
        
        # print("w, h:", w, h)
        
        BFS_now = deque([(w, h)])
        BFS_next = deque()
        pi = prefix[h][w]  # 이전에 이동한 거리에서 시작해야 함
        
        while BFS_now:
            nw, nh = BFS_now.popleft()
            
            # 도착한 경우, 결과에 이동횟수 추가
            if (nw, nh) == (H-1, W-1):
                result.append(prefix[nw][nh])
                break
        
            # 폰 이동: 상하좌우
            for i in range(4):
                pw = nw - dw2[i]
                ph = nh + dh2[i]
                    
                # 장애물이 아니고, 미방문이거나 값이 더 작으면
                if 0 <= pw < W and 0 <= ph < H:
                    if board[ph][pw] != 1 and (prefix[ph][pw] == 0 or
                                               pi + 1 < prefix[ph][pw]):
                        prefix[ph][pw] = pi + 1
                        BFS_next.append((pw, ph)) # 좌표 주의! 가로세로 반대로 적었음
                        
                        # 도착한 값이면 result에 추가
                        if (pw, ph) == (W-1, H-1):
                            result.append(prefix[ph][pw])
                            
            # BFS에서 다음 턴으로 이동
            if BFS_next != []:
                pi += 1
                BFS_now = BFS_next
                BFS_next = deque()
                
        # print("prefix:", prefix)
        # print("next:", next)
                    
    # 다음 턴으로 이동
    now = next
            
    # print("result:", result)
    # print("now:", now)


K = int(input())
W, H = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(H)]
prefix = [[0] * W for _ in range(H)]
prefix[0][0] = 1  # 시작점 방문 처리
 
# 현재 턴에 이동할 곳, 다음 턴에 이동할 곳
now = [(0, 0)]
next = []

w, h = 0, 0
result = []

# 나이트로 이동 가능한 곳들
dh = [-2, -1, 1, 2]
dw = [1, 2, 2, 1]

# 델타 탐색 순서: 오른쪽, 아래, 위, 왼쪽
dh2 = [0, 1, -1, 0]
dw2 = [1, 0, 0, -1]

# 나이트 이동
knight(board, W, H, w, h, dw, dh)

# print("result, now:", result, now)

# 도착 X, 이동 가능 O
if result == [] and now != []:
    # 폰 이동
    pawn(board, W, H, w, h, dw2, dh2)
    
print(prefix)
    
# 최소 이동횟수 출력
if result != []:
    print(min(result))
else:
    print(-1)

'''
문제 풀이:
말이 되고싶은 원숭이,
나이트가 되고싶은 폰

폰 r, c일 때
나이트(K번): 윗줄에서부터
(r-2, c-1), (r-2, c+1)
(r-1, c-2), (r-1, c+2)
(r+1, c-2), (r+1, c+2)
(r+2, c-1), (r+2, c+1)
폰(K번 이후): 델타로 이동

매트릭스:
0 0 0 0
1 0 0 0
0 0 1 0
0 1 0 0

최소이동:
0 1 2 3
-1 2 1 2
0 1 -1 3
0 -1 0 4
'''


'''
문제 정보:
0, 0 에서 H - 1, W - 1까지 이동

최소 이동 횟수를 매트릭스에 작성한다
K번 나이트 이동하고 나머지는 델타 이동

0은 평지, 1은 장애물
시작점, 도착점은 평지(0)

도착 불가능한 경우 result = -1
'''