import sys
sys.stdin = open('input_1231.txt')

# 완전이진트리를 순회한다
# 중위 순회 함수
def inorder(node):
    # 지정된 노드가 있으면
    if node:
        # L V R 순서로 순회한다
        # L = c1[node], V = parent[node], R = c2[node]
        inorder(c1[node])
        traversed_order.append(node)
        inorder(c2[node])

T = 10
# 트리가 갖는 정점의 수
for t in range(1, T + 1):
    N = int(input())
    graph = [input().split() for _ in range(N)]

    # 완전이진트리 그래프를 만든다
    # 부모, 자식1, 자식2 리스트
    parent = list(range(N + 1))
    c1 = [0] * (N + 1)
    c2 = [0] * (N + 1)

    # 문자 받기
    word = [0]

    # 부모 인덱스 1, 2, 3, ... 8(N)
    for i in range(N):
        # 저장값을 받을 때 오류나서 일단 보류...
        # vertex, stored_value, *child = input().split()

        # 문자 하나씩 받기
        word.append(graph[i][1])

        # ++ 존재할 때만 출력
        if len(graph[i]) >= 3:
            c1[i + 1] = int(graph[i][2])
        if len(graph[i]) == 4:
            c2[i + 1] = int(graph[i][3])
        if len(graph[i]) == 2:
            pass

    # 순회하는 순서대로 값을 도출한다
    traversed_order = []
    inorder(1)

    result = []
    # 중위 순서한 순서대로 문자를 배열
    for char in range(N):
        num = traversed_order[char]
        result.append(word[num])

    result_join = ''.join(result)

    print(f'#{t} {result_join}')