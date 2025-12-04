import sys
sys.stdin = open('input')

# 중위탐색으로 가장 먼저 탐색되는 곳에 1부터 값을 저장한다
# 부모가 1, N//2인 경우의 저장값을 출력한다
def Inorder(node):
    Inorder[left_num]
    print(node)
    Inorder[right_num]

T = int(input())
for t in range(1, T + 1):
    N = int(input())

    # 완전 이진 트리를 만든다
    # 부모 노드
    parent = [0]
    for i in range(1, N + 1):
        parent.append(i)

    # 자식 노드
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    # 왼쪽 노드
    for j in range(1, N + 1):
        # 왼쪽 노드는 노드 번호 i면 (i * 2)
        if j % 2 == 0:
            left_num = int(j/2)
            left[left_num] = j
    
    # 오른쪽 노드
    for k in range(1, N + 1):
        # 오른쪽 노드는 노드 번호 i면 (i * 2) + 1
        if k % 2 == 1:
            right_num = int(k//2)
            right[right_num] = k
        right[0] = 0

    print(f'#{t} {Inorder(1)} {Inorder(N//2)}')