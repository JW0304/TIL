import sys
sys.stdin = open('input_5249.txt')

def find(x):
    # 다를 경우 재귀함수로 대표자 구하기
    if x != parent[x]:
        parent[x] = find(parent[x])
        return parent[x]
    # 같을 경우 그대로 대표자 반환
    else:
        return parent[x]
    
def union(a, b):
    par_a, par_b = find(a), find(b)
    if par_a < par_b:
        parent[par_b] = par_a
    else:
        parent[par_a] = par_b

T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    
    # 간선 리스트를 만든다
    edge_list = []
    
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edge_list.append([n1, n2, w])
        
    # 간선 리스트를 오름차순으로 정렬한다
    edge_list.sort(key=lambda x: x[2])
    
    # 노드의 대표자 리스트를 만든다
    parent = list(range(V + 1))
    
    edge_count = 0
    edge_sum = 0
    
    for i in range(E):
        # 가중치가 작은 간선부터 하나씩 선택
        # find로 n1과 n2의 대표자가 다르면 union으로 연결
        r1 = find(edge_list[i][0])
        r2 = find(edge_list[i][1])
        if r1 != r2:
            union(r1, r2)
            edge_count += 1
            edge_sum += edge_list[i][2]
        # 선택한 간선이 N - 1보다 작을 동안, N = V + 1
        if edge_count == V:
            break
    
    # 간선의 가중치의 합 출력
    print(f'#{t} {edge_sum}')