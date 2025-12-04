import sys
sys.stdin = open('input_5189.txt')

from itertools import permutations

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    arr = list(range(2, N + 1))
    # 리스트에서 원소 개수가 N - 1개인 순열
    perm_list = list(permutations(arr, N - 1))

    print(f'#{t} {perm_list}')