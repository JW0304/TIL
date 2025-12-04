# 2025-03-19
# 오후 3:19
# SWEA 5247 연산

import sys
sys.stdin = open('input_5247.txt')

from collections import deque

def bfs(start_num, target_num):
    q = deque([(start_num, 0)])
    visited = [0] * (10 ** 6 + 1)
    while q:
        temp_num, count = q.popleft()
        visited[temp_num] = 1
        if temp_num == target_num:
            return count
        for next_num in [temp_num + 1, temp_num - 1, temp_num * 2, temp_num - 10]:
            if 1 <= next_num <= 10 ** 6 and not visited[next_num]:
                visited[next_num] = 1
                q.append((next_num, count + 1))

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())

    print(f'#{t} {bfs(N, M)}')
