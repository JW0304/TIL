# SWEA
# sum
# 2025-02-17 월 
# 04:16 - 05:42

import sys
sys.stdin = open('input_sum.txt')

'''
어떻게 구하지?
가로의 합: 2중 for문, 가로 고정, 세로 변화 -> 각 행마다 합 초기화
세로의 합: 2중 for문, 세로 고정, 가로 변화 -> 각 열마다 합 초기화
대각선의 합 (diagonal): 가로세로 순이동 / 역이동
최대값 비교: max, list, a[0] 등 / 비교, 갱신, 교환

00 01 02 ... 0,99
10 11 12    1,98
20 21 22
...
  98,1
99,0        99,99

if N=100: n=0,1,2,...,99
\ 방향: arr[n][n] for n in range(N)
/ 방향: arr[99-n][n] for n in range(N)
'''

'''
틀린 부분:
가로, 세로는 여러 줄이므로
최댓값을 반환해야 함

// 반복문 들여쓰기: 순회, 순회 끝나면 한 줄씩 다음 연산 처리
'''

def row_sum(arr):
    # 함수가 실행될 때마다(각 예시마다) 초기화
    max_r = 0
    for r in range(N):  # 0, 1, 2 ...
        sum_r = 0  # r 고정, c 변화 / 각 r 마다 합 초기화
        for c in range(N):  # 00, 01, 02 / 10, 11, 12 ...
            sum_r += arr[r][c]
        # 다음 행으로 이동하기 전에 최댓값 갱신 / 이거 없으면 그냥 마지막 값 반환!!
        max_r = max(max_r, sum_r)
    return max_r  # sum 이 아니라 max 여야 함!!

def col_sum(arr):
    max_c = 0
    for c in range(N):  # 0, 1, 2 ...
        sum_c = 0  # c 고정, r 변화 / 각 c 마다 합 초기화
        for r in range(N):  # 00, 10, 20 / 01, 11, 21 ...
            sum_c += arr[r][c]
        # 다음 열로 이동하기 전에 최댓값 갱신
        max_c = max(max_c, sum_c)
    return max_c

# / 방향(우상향) 대각선
def diag_sum_up(arr):
    sum_du = 0
    for n in range(N):
        sum_du += arr[N-1-n][n]  # 99가 아니라 N-1-n으로 해야 
    return sum_du
    
# \ 방향(우하향) 대각선
def diag_sum_down(arr):
    sum_dd = 0
    for n in range(N):
        sum_dd += arr[n][n]
    return sum_dd

T = 10
N = 100
for t in range(1 , T+1):
    tc = int(input())  # 사용 안해도 됨
    arr = [list(map(int, input().split())) for _ in range(N)]  # 0 ~ 99

    result = max(row_sum(arr), col_sum(arr), diag_sum_up(arr), diag_sum_down(arr))
    # 하나의 테스트케이스(반복문)에 대해
    print(f'#{t} {result}')