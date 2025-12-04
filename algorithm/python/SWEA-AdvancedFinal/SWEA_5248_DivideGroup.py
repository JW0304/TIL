import sys
sys.stdin = open('input_5248.txt')

# union으로 같은 그룹으로 묶는다
def union(a, b):
    # 각각의 대표자를 찾아서 연결한다
    a_par = find(a)
    b_par = find(b)
    # 더 작은 수를 대표자로 정한다
    if a_par < b_par:
        parent[b_par] = a_par
    else:
        parent[a_par] = b_par

# find로 대표자를 찾는다
def find(x):
    # 같을 경우 대표자 반환
    if x == parent[x]:
        return parent[x]
    # 다를 경우 재귀함수 이후 대표자 반환
    else:
        parent[x] = find(parent[x])
        return parent[x]

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # 대표자 리스트를 만든다
    parent = list(range(N + 1))
    
    for i in range(M):
        # 신청서의 (a, b) 쌍을 
        a = arr[2 * i]
        b = arr[2 * i + 1]
        
        # union으로 같은 그룹으로 묶는다
        union(a, b)
    
    # 모든 원소에 대해 find로 대표자를 찾는다
    for j in range(1, N + 1):
        find(j)
    
    # 0을 제외하고 리스트에서 조의 수를 세서 출력한다 
    # 리스트[1:] -> 집합 -> 길이
    count = len(set(parent[1:]))
    
    print(f'#{t} {count}')