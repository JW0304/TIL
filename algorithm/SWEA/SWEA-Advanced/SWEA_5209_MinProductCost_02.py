# 2025-03-18
# 오후 2:35
# SWEA 5209 최소 생산 비용

import sys
sys.stdin = open('input_5209.txt')

'''
어렵..
'''

def choose_factory(row):
    global temp_cost
    global min_cost

    if temp_cost >= min_cost:
        return
    
    if row == N:
        min_cost = min(min_cost, temp_cost)
        return
    
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            temp_cost += matrix[row][i]
            choose_factory(row + 1)
            # 원상복구
            temp_cost -= matrix[row][i] 
            visited[i] = 0

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 최소 비용
    min_cost = float('inf')
    temp_cost = 0
    visited = [0] * N
    choose_factory(0)

    print(f'#{t} {min_cost}')