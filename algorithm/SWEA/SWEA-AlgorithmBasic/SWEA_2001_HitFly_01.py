# SWEA
# 2001. 파리퇴치
# 2025-02-17 월 
# 03:48

'''
N x N 크기의 배열에서 (5 ~ 15)
M x M 크기의 파리채 (2 ~ N)
파리(flies): 1 ~ 30
'''
import sys
sys.stdin = open('input_fly.txt')  # 따옴표 왜 필요?

'''
모든 요소를 순회하는 법: 2중 for문:
for i in range(N):
    for j in range(N):
        arr[i][j]
위와 같이 i를 고정시키고 j, 또는 j를 고정시키고 i를 순회한다

        [00 01 02] i = 0
        [10 11 12] i = 1
        [20 21 22] i = 2
      j = 0, 1, 2
'''

T = int(input())

# 여러 개의 배열과 파리채(예시 입력)에 대해:
for t in range(1, T + 1):
    N, M = map(int, input().split())  # split and strip are different methods
    # 리스트 컴프리헨션 방법은? 여러개의 줄로 된 입력을 받는 방법은?
    # 이차원 리스트, 이차원 배열? 이름이 뭐였는지..
    arr = [list(map(int, input().split())) for _ in range(N)]  # from 0 to 4 (if N = 5)

    '''
    1. N - M + 1 범위에서 N을 순회 -> 2중 for문을 사용 (i, j 사용 등)
    2. 파리채의 범위 내에서 값을 더함 -> 2중 for문 사용 (r, c / x, y 등)
    3. 값을 더한 것들 중 최댓값을 구함 -> max, list.append, a[0]과 a[1]~[n] 비교 등
    '''

    max_value = 0 # for문으로 순회하기 전에 초기화 (새로운 배열)
    # 배열 내에서 파리채의 이동 범위, 전체적 합계(최댓값)
    for i in range(N-M+1):  # if N=5, M=3, i = 0, 1, 2 ...
        for j in range(N-M+1): # same, ij = 00, 01, 02 ...
            
            temp_sum = 0 # for문으로 순회하기 전에 초기화 (새로운 파리채 범위)
            # 파리채 내의 범위, 일시적 합계
            for r in range(M):  # if M=3: x = 0, 1, 2
                for c in range(M):  # same: xy = 00, 01, 02 / 10, 11, 12 ...
                    temp_sum += arr[i + r][j + c]

            # 배열 내에서 / 일시적 합계와 최댓값 비교, 교환 // 최댓값 구하는 법: 목록, 비교, 갱신, 교환 등
            if temp_sum > max_value:
                max_value = temp_sum  # 순서 바꾸면 안됨! "변수 = 값"

    print(f'#{t} {max_value}')
