# 2025-03-15
# 오후 6:33
# SWEA 5176 이진탐색

import sys
sys.stdin = open('input_5176.txt')

# 중위순서의 순서에 따라 값 + 1
def inorder(node):
    global count
    if node != 0:  # 노드가 0이 아닐 때만 탐색을 계속함
        inorder(left[node])
        count += 1
        value[node] = count  # 노드 번호의 자리에 값을 저장
        inorder(right[node])
    return count

T = int(input())
for t in range(1, T + 1):
    # 저장값 N = 노드의 수 V
    V = int(input())
    E = V - 1
    
    left = [0] * (V + 1)
    right = [0] * (V + 1)
    # 자식인 2부터 V까지
    for child in range(2, V + 1):
        if child % 2 == 0:
            left[child//2] = child
        else:
            right[child//2] = child
    count = 0
    value = [0] * (V + 1)
    inorder(1)
    
    print(f'#{t} {value[1]} {value[V//2]}')