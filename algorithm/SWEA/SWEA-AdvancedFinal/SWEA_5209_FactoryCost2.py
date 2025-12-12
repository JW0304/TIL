import sys
sys.stdin = open('input_5209.txt')

# 현재의 상품 번호, 카운트를 변수로 가짐
# 트리는 (상품 -> 공장) * N 개와 같음
def dfs(product, count):
    global result
    
    # 카운트가 결과값보다 클 경우 가지치기
    # (해당하는 트리의 가지는 볼 필요가 없음)
    if count >= result:
        return
    
    # 카운트가 결과값보다 작고 상품 번호가 N일 경우
    # (트리에서 상품 번호가 N과 같을 경우)
    if product == N:
        result = count
    
    # 각각의 공장에 대해 방문처리 후 백트래킹
    # (트리의 가지들을 탐색하기)
    for factory in range(N):
        if visited[factory] == 0:
            visited[factory] = 1
            # 단말 노드까지 재귀로 탐색
            dfs(product + 1, count + matrix[product][factory])
            visited[factory] = 0

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    # 공장 방문 리스트
    visited = [0] * N
    
    # 초기화
    result = float('inf')
    # 상품 번호, 카운트
    dfs(0, 0)
    
    print(f'#{t} {result}')