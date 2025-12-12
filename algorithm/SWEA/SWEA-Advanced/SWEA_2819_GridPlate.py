# 2025-03-14
# 오전 11:18
# SWEA 2819 격자판 숫자 이어붙이기

import sys
sys.stdin = open('input_2819.txt')

def travel(temp_r, temp_c, one_number):
    if len(one_number) == 7:
        numbers.add(one_number)
        return
    
    for i in range(4):
        nr = temp_r + dr[i]
        nc = temp_c + dc[i]
        if 0 <= nr < 4 and 0 <= nc < 4:
            travel(nr, nc, one_number + grid[nr][nc])

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for t in range(1, T + 1):
    grid = [list(map(str, input().split())) for _ in range(4)]
    numbers = set()

    for r in range(4):
        for c in range(4):
            one_number = grid[r][c]
            travel(r, c, one_number)

    print(f'#{t} {len(numbers)}')

    # 한 자리마다 6번 이동, 4 ** 6 = 4,096
    # 16자리이므로 4 ** 8 = 65,536
