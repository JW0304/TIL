# 2025-03-16
# 오후 11:28
# SWEA 4837 부분집합의 합

import sys
sys.stdin = open('input_4837.txt')

T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(range(1, 13))
    length = len(A)
    
    result = 0
    for i in range(1 << 12):            # 1 << 12 = 2 ** 12 = 4096, i = 0 ~ 4095, 모든 부분집합에 대해
        subset = []                     # 4096개의 각 부분집합에 대해
        elements_sum = 0                # 원소의 합
        for j in range(length):         # 주어진 배열(부분집합의 수를 구할 배열)의 인덱스, 원소가 12개이므로 0, 1, 2, ... 11
            if i & (1 << j):            # i = 0000, 0001, 0010, 0011, 0100, ... (= 0, 1, 2, 3, 4...) 이고, 각 비트 1은 포함하는 원소를 뜻함
                                        # j = 0, 1, 2, ... 라면 1 << j는 1, 10, 100... 순으로 A의 원소가 배열됨
                subset.append(A[j])     # 부분집합에 포함된다면 (i & (1 << j)라면) 부분집합에 넣기
                elements_sum += A[j]    # 부분집합의 합에 더하기
        if len(subset) == N and elements_sum == K:  # 주어진 원소의 수, 원소의 합과 같다면
            result += 1                 # 결과값을 + 1 한다
            
    print(f'#{t} {result}')





# 강사님 코드 - 비트연산 
# T = int(input())
# for t in range(1, T + 1):
#     N, K = map(int, input().split())
#     result = 0
    
#     # 1부터 12까지의 숫자 리스트
#     arr = list(range(1, 13))

#     # 2^12 = 4096 가지 부분집합 전부 탐색
#     for subset_mask in range(1 << len(arr)):  
#         tmp = []
#         for j in range(len(arr)):
#             # subset_mask의 j번째 비트가 1이면 arr[j]를 부분집합에 포함
#             if subset_mask & (1 << j):
#                 tmp.append(arr[j])

#         # 부분집합 tmp가 원소 N개, 합이 K인가 검사
#         if len(tmp) == N and sum(tmp) == K:
#             result += 1
    
#     print(f'#{t} {result}')
    
# 강사님 코드 - 재귀
# def recur(idx, arr):
#     global result
    
#     # 배열 nums의 끝(12개 숫자 모두 확인)까지 도달했을 때
#     if idx == 12:
#         # 부분집합 arr의 길이가 N이고, 합이 K라면 카운트 증가
#         if len(arr) == N and sum(arr) == K:
#             result += 1
#         return

#     # 1) 현재 idx에 해당하는 원소(nums[idx])를 '포함'하는 경우
#     arr.append(nums[idx])
#     recur(idx + 1, arr)

#     # 2) 현재 idx에 해당하는 원소를 '포함하지 않는' 경우
#     arr.pop()
#     recur(idx + 1, arr)

# T = int(input())

# for tc in range(1, T+1):
#     N, K = map(int, input().split())

#     # 1부터 12까지의 숫자
#     nums = list(range(1, 13))
#     result = 0

#     # 초기 상태에서 idx=0(첫 원소), 부분집합 arr=[](비어 있음)
#     recur(0, [])

#     print(f'#{tc} {result}')
