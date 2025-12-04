import sys
sys.stdin = open('input_5209.txt')

def dfs(product, count):
    global result
    
    # 가지치기(더 이상 트리 탐색할 필요 없음)
    if count >= result:
        return
    
    # count가 result보다 작고 상품 개수가 N일 때
    if product == N:
        result = count
        return
    
    for factory in range(N):
        if visited[factory] == 0:
            visited[factory] = 1
            # 단말 노드까지 재귀함수로 탐색
            dfs(product + 1, count + matrix[product][factory])
            
            # 백트래킹으로 트리를 탐색(방문 되돌리기)
            visited[factory] = 0
    
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 공장 방문 확인 리스트
    visited = [0] * N
    result = float('inf')
    
    # 첫번째 제품 (인덱스 0)
    dfs(0, 0)
    
    print(f'#{t} {result}')