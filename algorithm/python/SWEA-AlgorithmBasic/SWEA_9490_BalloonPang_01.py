# SWEA
# 9490. 풍선팡
# 2025-02-17 월 
# 07:42
'''
가운데 숫자만큼 주변의 풍선이 터진다
가운데 숫자가 n 이라면 상하좌우로 n 개가 터진다

00 01 02 03
10 11 12 13
20 21 22 23
30 31 32 33

'''

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t} {result}')