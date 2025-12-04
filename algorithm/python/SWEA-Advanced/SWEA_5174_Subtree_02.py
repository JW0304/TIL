# 2025-03-12
# 오전 10:15
# SWEA 5174 subtree

import sys
sys.stdin = open('input_5174.txt')

# 이진 트리에서 특정한 노드 N을 루트로 하는 서브트리 구하기

def preorder(node):
    global count  # 함수 밖의 count를 가져옴
    if node:      # node가 존재하면 (0이 아닌 값을 가지면)
        # 할일 처리(프린트, 카운트, append 등): 전위 순회이므로 맨 앞에 온다
        count += 1
        preorder(left[node])
        preorder(right[node])

T = int(input())
for t in range(1, T + 1):
    # < 입력 >
    # 간선의 개수 E, 루트가 될 노드 N
    E, root = map(int, input().split())
    # 부모 자식 노드의 쌍
    # 예를 들어 2를 부모로 하는 쌍은 2 1, 2 5 와 같음
    pairs = list(map(int, input().split()))

    # < 트리 만들어주기 >
    # 노드 수는 (간선의 개수 + 1), 즉 E + 1
    num = E + 1
    left = [0] * (num + 1)
    right = [0] * (num + 1)

    # 간선의 수만큼 쌍이 있음
    for i in range(E):
        p = pairs[2 * i]
        c = pairs[2 * i + 1]
        
        # 부모 노드를 인덱스로 자식 노드를 구하기
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    # < 순회 함수 >
    # 각 트리, 루트에서 서브트리를 순회
    count = 0
    preorder(root)
    # 함수가 종료되면 count를 출력
    print(f'#{t} {count}')