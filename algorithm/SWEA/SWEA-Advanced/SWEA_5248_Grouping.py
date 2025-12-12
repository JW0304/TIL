# 2025-03-19
# 오전 9:15
# SWEA 5248 그룹 나누기

import sys
sys.stdin = open('input_5248.txt')



# 1. 서로소 집합으로 풀기

# 자기 자신을 부모로 하는 집합
def make_set(num):
    # 부모 != 대표자(대표자는 부모를 거슬러 올라간 루트 노드)
    parents = list(range(num + 1))
    return parents

# 대표자를 찾는 함수
def find_rep(child):
    # 부모와 자식이 같을 경우 대표자 반환
    if child == parents[child]:
        return child
    
    # 경로 압축(child의 부모를 대표자로 설정)
    # parents[child] = find_rep(parents[child])
    # return parents[child]
    
    # if 조건에 맞지 않으면 재귀함수 반환하면 됨
    # else:
    #     while num != parents[num]:
    #         find_rep(parents[num])

    # if 조건에 맞지 않는 동안 재귀
    return find_rep(parents[child])

# 각각의 대표자를 찾아서 연결하는 함수
# y의 대표자를 x의 대표자로 설정
def union(x, y):
    rep_x = find_rep(x)
    rep_y = find_rep(y)

    # 같은 집합일 경우 할 필요가 없음
    if rep_x == rep_y:
        return

    # 병합 조건에 따라
    # 더 작은 번호의 노드를 대표자로 할 경우
    if rep_x < rep_y:
        parents[rep_y] = rep_x
    else:
        parents[rep_x] = rep_y

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    pairs = list(map(int, input().split()))

    # 부모 집합을 만든다
    parents = make_set(N)

    # 주어진 쌍에서 부모, 자식 찾기
    for i in range(M):
        p = pairs[2 * i]
        c = pairs[2 * i + 1]

        # 병합 함수 실행
        union(p, c)

    # 부모가 아닌 대표자의 개수를 세야 함
    # result_set = set(parents)

    # 대표자가 원소와 같은 경우에만 카운트를 더함
    count = 0
    for j in range(1, N + 1):
        if find_rep(j) == j:
            count += 1

    print(f'#{t} {count}')



# 2. 스택으로 풀기

# def visit(v):
#     global stack
#     if visited[v] == 0:
#         visited[v] = 1
#         stack.extend(adj[v])
#     while stack:
#         next = stack.pop()
#         visit(next)

# T = int(input())
# for t in range(1, T + 1):
#     N, M = map(int, input().split())
#     pairs = list(map(int, input().split()))

#     # 인접 리스트
#     adj = [[] for _ in range(N + 1)]

#     # 쌍에서 짝수와 홀수의 값들, 인접 리스트에 저장
#     for i in range(M):
#         p = pairs[2 * i]
#         c = pairs[2 * i + 1]
#         adj[p].append(c)
#         adj[c].append(p)

#     # 방문한 곳들을 체크
#     visited = [0] * (N + 1)

#     # 인접한 곳 방문, 조 카운트
#     count = 0
#     for num in range(1, N + 1):
#         stack = []
#         if visited[num] == 0:
#             visit(num)
#             count += 1

#     print(f'#{t} {count}')