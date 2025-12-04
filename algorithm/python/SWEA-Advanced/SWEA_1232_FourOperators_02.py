# 2025-03-15 토
# 오후 10:17
# SWEA 1232 사칙연산

import sys
sys.stdin = open('input_1232.txt')

def operate(node):
    if node != 0 and left[node] != 0 and right[node] != 0:
        operate(left[node])
        operate(right[node])
        left_value, right_value = value[left[node]], value[right[node]]
        if operator[node] == '+':
            value[node] = left_value + right_value
        elif operator[node] == '-':
            value[node] = left_value - right_value
        elif operator[node] == '*':
            value[node] = left_value * right_value
        elif operator[node] == '/':
            value[node] = left_value / right_value
    
T = 10
for t in range(1, T + 1):
    N = int(input())
    
    # 완전이진트리가 아니므로 노드번호는 임의
    tree = [list(input().split()) for _ in range(N)]
    
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    value = [0] * (N + 1)
    operator = [0] * (N + 1)
    
    for i in range(N):
        if len(tree[i]) == 4:
            operator[i + 1] = tree[i][1]
            left[i + 1] = int(tree[i][2])
            right[i + 1] = int(tree[i][3])
        else:
            value[i + 1] = int(tree[i][1])
    
    operate(1)
    print(f'#{t} {int(value[1])}')