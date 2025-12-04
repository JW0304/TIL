import sys
sys.stdin = open('input_1251.txt')

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
        return parent[x]
    else:
        return parent[x]
    
def union(a, b):
    rep_a, rep_b = find(a), find(b)
    if rep_a != rep_b:
        if rep_a < rep_b:
            parent[rep_b] = rep_a
        else:
            parent[rep_a] = rep_b

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    E = float(input())

    # 간선 리스트
    w_list = 0
    # 간선 리스트를 오름차순으로 정렬

    # 대표자 리스트
    parent = list(range(N))


    # 최소 신장 트리에서 가중치의 합의 제곱
    L = 0

    # 소수 첫째 자리에서 반올림, 정수로 출력
    result = E * (L ** 2)

    print(f'#{t} {int(result)}')