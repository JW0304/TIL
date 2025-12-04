import sys
sys.stdin = open('input_subsetsum.txt')

arr = list(map(int, input().split()))
arr.sort()
subsets = []

n = len(arr)
for i in range(1 << n):  # 1을 n만큼 민다 (1 = True, 2 ** n 자리가 True)
    subset = []
    for j in range(n):
        if i & (1 << j):
            subset.append(arr[j])
    if subset and sum(subset) == 0:
        subsets.append(subset)
        
print(subsets)