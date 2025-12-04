import sys
sys.stdin = open('input_5189.txt')

def dfs():
    pass
    
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 위치 방문
    visited = [0] * N
    # 최소 소비량
    result = float('inf')
    
    print(f'#{t} {result}')

# -------------------------------
# 문제풀이

import itertools

T = int(input())  # 테스트 케이스 개수 입력

for case_num in range(1, 1 + T):
    N = int(input())  # 정점 개수 입력
    data = [list(map(int, input().split())) for _ in range(N)]  # 배터리 소비량 행렬 입력

    arr = list(range(2, N + 1))  # 2부터 N까지의 정점 리스트 생성
    permutations_list = itertools.permutations(arr, N - 1)  # 1을 제외한 순열 생성 (리스트 변환 불필요)

    min_price = float('inf')  # 최소 배터리 소비량을 저장할 변수 (초기값: 매우 큰 값)

    # 가능한 모든 경로의 배터리 소비량 계산
    for case in permutations_list:
        case = (1,) + case + (1,)  # 시작점(1)과 도착점(1) 추가
        price = sum(data[case[i] - 1][case[i + 1] - 1] for i in range(N))  # 경로의 배터리 소비량 합산

        min_price = min(min_price, price)  # 최소 배터리 소비량 갱신

    # 결과 출력
    print(f"#{case_num} {min_price}")
