# 2025-03-12
# 오전 10:54
# SWEA 5176 이진탐색

import sys
sys.stdin = open('input_5176.txt')

def inorder(node):
    global count
    if node:
        inorder(c1[node])
        count += 1
        store[node] = count
        inorder(c2[node])

T = int(input())
for t in range(1, T + 1):
    # 주어진 자연수 N (총 노드 수)
    N = int(input())

    c1 = [0] * (N + 1)
    c2 = [0] * (N + 1)

    # 부모를 인덱스로 자식 노드를 구함
    '''
    완전 이진 트리
    p   0 1 2 3 4 5 6
    c1 [0 2 4 6 0 0 0]
    c2 [0 3 5 0 0 0 0]
    왼쪽 자식은 p * 2
    오른쪽 자식은 p * 2 + 1
    '''

    for p in range(1, N + 1):
        if p * 2 <= N:
            c1[p] = p * 2
        if p * 2 + 1 <= N:
            c2[p] = p * 2 + 1
        else:
            break
    
    # 부모를 인덱스로 한 저장값, 중위 순회로 저장
    store = [0] * (N + 1)
    count = 0
    # 노드 1부터 중위순회 시작
    inorder(1)

    print(f'#{t}',store[1],store[N//2])