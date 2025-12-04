import sys
sys.stdin = open('input_subsetsum.txt')

arr = list(map(int, input().split()))
arr.sort()
subsets = []

N = len(arr)
# i -> 2 ** N, 모든 경우의 수
# 1024개
for i in range(1 << N):
    # 모든 경우의 수에 해당하는 부분집합
    subset = []
    # j -> N, 전체 집합의 원소의 개수
    for j in range(N):
        # 이 경우의 수(부분집합)에 j 자리의 원소가 포함될 경우
        if i & (1 << j):
            subset.append(arr[j])
    
    # 공집합이 아니고 합이 0인 경우
    if subset and sum(subset) == 0:
        subsets.append(subset)

print(subsets)