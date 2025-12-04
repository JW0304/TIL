# 2025-03-09 일
# 오후 12:09

import sys
sys.stdin = open('input_1232.txt')

'''
입력:
정수값 - 정점, 양의 정수
연산자, 자식노드 - 정점, 연산자, 왼쪽자식, 오른쪽자식

실수로 계산, 정수로 출력

tree[0] = node, tree[1] = value/operator
tree[2] = left, tree[3] = right
'''

# 후위 순회, 양쪽값과 연산자를 계산
def postorder(node):
    if node:
        postorder(left[node])
        postorder(right[node])
        node_order.append(node)

T = 10
for t in range(1, T + 1):
    N = int(input())
    tree = [list(input().split()) for _ in range(N)]
    
    node = [range(0, N + 1)]
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    operator = [0] * (N + 1)
    value = [0] * (N + 1)
    
    for i in range(N):
        if len(tree[i]) == 4:
            left[i + 1] = int(tree[i][2])
            right[i + 1] = int(tree[i][3])
            operator[i + 1] = tree[i][1]
        
        # 길이가 2인 경우
        else:
            value[i + 1] = int(tree[i][1])
            
    # 후위 순회된 노드의 순서
    # node_order로 나옴
    node_order = []
    postorder(1)
    
    # left, right, operator 순으로 계산되어야 함
    # 후위 순회이므로 스택으로 넣고 연산자가 나오면 2개 빼서 계산
    stored_value = []
    stack = []

    for j in range(N):
        # 정수인 경우
        if value[node_order[j]] != 0:
            stored_value.append(value[node_order[j]])
        # 연산자인 경우
        else:
            stored_value.append(operator[node_order[j]])

    # 스택에서 빼면서 계산
    for num in range(N):
        # 숫자인 경우
        if str(stored_value[num]).isdigit() == True:
            stack.append(stored_value[num])
        # 연산자인 경우
        else:
            right_num = stack.pop()
            left_num = stack.pop()
            if stored_value[num] == '+':
                stack.append(left_num + right_num)
            elif stored_value[num] == '-':
                stack.append(left_num - right_num)
            elif stored_value[num] == '*':
                stack.append(left_num * right_num)
            elif stored_value[num] == '/':
                stack.append(left_num / right_num)

    print(f'#{t}',int(stack[0]))