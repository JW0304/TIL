# 2025-03-02
# 오후 2:57 - 3:38 (풀이 자체)
# 오후 3:44 (디버깅으로 검토)
# 오후 3:55 (다른 사람들 풀이)
# SWEA 9490 풍선팡

'''
가운데가 1이면 상하좌우 1씩,
가운데가 2면 상하좌우 2씩 터진다
'''

import sys
sys.stdin = open('input_9490.txt')

# 상하좌우 델타탐색
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for t in range(1, T + 1):
    
    # N줄에 걸쳐 M개의 풍선 (N행 M열, NxM 행렬(matrix))
    N, M = map(int, input().split())
    # N행의 풍선, 2차원 배열
    balloons = [list(map(int, input().split())) for _ in range(N)]
        
    # 각 테스트케이스마다 최대 종이 꽃가루 개수
    max_flower = 0
    
    # 모든 행과 열의 풍선에 대해
    for r in range(N):
        for c in range(M):
            
            # 가운데 풍선의 숫자
            middle_balloon = balloons[r][c]
            
            # 종이 꽃가루 개수 초기화, 가운데 풍선의 수를 더함
            one_flower = middle_balloon
            
            # 상하좌우로 가운데 꽃가루 수만큼 이동해서 탐색
            # 풍선이 사방으로 터진다면
            
            # 길이가 3일 때, 사방으로 3만큼 이동
            for length in range(1, middle_balloon + 1):
                
                # 사방으로 길이만큼 이동한다
                for i in range(4):
                    # dr, dc는 리스트이므로 인덱스값을 줘야 한다!
                    nr = r + (dr[i] * length)
                    nc = c + (dc[i] * length)
                                    
                    # 구한 값이 범위 안에 있을 때
                    if 0 <= nr < N and 0 <= nc < M:
                        # 각 가운데 풍선에서 터진 값을 더한다
                        one_flower += balloons[nr][nc]
                        
            # 각 풍선마다 최대값을 갱신한다
            if one_flower > max_flower:
                max_flower = one_flower
    
    print(f'#{t} {max_flower}')