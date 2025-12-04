# 2025-03-15
# 오후 11:58
# SWEA 7465 창용 마을 무리의 개수

import sys
sys.stdin = open('input_7465.txt')

def count_group(graph):
    global group
    for i in range(1, N + 1):
        if visited[i] == 0:
            visited[i] = 1
            visit = graph[i]
            while visit:
                adj = visit.pop()
                if visited[adj] == 0:
                    visited[adj] = 1
                    visit.extend(graph[adj])
            group += 1
    return group
                
T = int(input())
for t in range(1, T + 1):
    # 마을의 사람 수, 서로를 알고 있는 관계 수
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(M)]
    
    graph = [[] for p in range(N + 1)]
    visited = [0] * (N + 1)
    
    for i in range(M):
        graph[arr[i][0]].append(arr[i][1])
        graph[arr[i][1]].append(arr[i][0])
    
    group = 0
    print(f'#{t} {count_group(graph)}')