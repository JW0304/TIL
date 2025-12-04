# 2025-03-15
# 오후 7:00
# SWEA 1231 중위순회

import sys
sys.stdin = open('input_1231.txt')

# 중위순회로 저장된 문자열을 출력한다
def inorder(node):
    # local -> global, + -> += (재할당)
    global word
    if node:
        inorder(left[node])
        word += value[node]
        inorder(right[node])
    return word
    
T = 10
for t in range(1, T + 1):
    V = int(input())
    E = V - 1
    input_info = [list(input().split()) for _ in range(V)]
    
    left = [0] * (V + 1)
    right = [0] * (V + 1)
    value = [0] * (V + 1)
    
    # 완전 이진 트리이므로 노드 번호는 저장할 필요 없음
    for i in range(V):
        value[i + 1] = input_info[i][1]
    
    for c in range(2, V + 1):
        if c % 2 == 0:
            left[c//2] = c
        else:
            right[c//2] = c
            
    word = str()
    print(f'#{t} {inorder(1)}')