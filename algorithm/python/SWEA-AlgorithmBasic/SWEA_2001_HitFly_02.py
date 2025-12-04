# 2025-03-02
# 오후 3:58 - 4:20 (풀이 자체)
# 오후 4:28 (검토)
# SWEA 2001 파리퇴치

'''
NxN 배열에 MxM 크기의 파리채를 내려친다
파리채를 내리칠 수 있는 범위는 N - M + 1 까지
파리채의 범위는 range(M), 크기가 3이면 0, 1, 2
'''

import sys
sys.stdin = open('input_2001.txt')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    # 각 테스트케이스마다 최대 파리개수
    max_fly = 0
    
    # 행렬의 모든 부분을 범위 내에서 순회
    for r in range(N - M + 1):
        for c in range(N - M + 1):
            # 기준이 되는 위치, 파리채의 왼쪽 위
            start_location = matrix[r][c]
            
            # 각 파리채의 위치마다 파리수를 초기화
            one_fly = 0
            
            # 기준이 되는 위치부터 파리채의 범위
            for hit_r in range(M):
                for hit_c in range(M):
                    # 위치를 시작점에 따라 옮겨줘야 함!
                    nr = r + hit_r
                    nc = c + hit_c
                    # 각 파리수를 더함
                    one_fly += matrix[nr][nc]
            
            # 테스트케이스별 최대 파리수
            if one_fly > max_fly:
                max_fly = one_fly
    
    print(f'#{t} {max_fly}')