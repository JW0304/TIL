# 2025-03-02
# 오후 1:51
# SWEA 4828 min max

'''
최댓값, 최솟값을 배열의 가장 첫번째 값으로 설정해도 됨!
'''

import sys
sys.stdin = open('input_4828.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    
    # 가장 큰 수를 순회하며 구한다
    max_num = 0
    for i in range(len(numbers)):
        if max_num <= numbers[i]:
            max_num = numbers[i]
    
    # 가장 큰 수에서 차례대로 내려간다
    min_num = max_num
    
    # 가장 작은 수를 순회하며 구한다
    for j in range(len(numbers)):
        if min_num >= numbers[j]:
            min_num = numbers[j]
    
    # 가장 큰 수와 가장 작은 수의 차이를 출력한다
    print(f'#{t} {max_num - min_num}')