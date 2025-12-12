import sys
sys.stdin = open('input_5208.txt')

# dfs 탐색 (백트래킹), 재귀함수
def dfs(location, level):  # 현재의 위치, 트리의 레벨
    global min_chrg
    
    # 가지치기, 트리의 레벨이 최솟값보다 커지는 경우
    if level >= min_chrg:
        return
    
    # 도착했을 때
    if location >= N - 1:
        min_chrg = level
        return
    
    # 현재 위치에서 이동할 수 있는 범위
    for move in range(1, charger[location] + 1):
        dfs(location + move, level + 1)

T = int(input())
for t in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = arr[0]
    charger = arr[1:]
    
    # 최소 충전횟수 초기화
    min_chrg = float('inf')
    # 시작 위치 0, -1부터 카운트
    dfs(0, -1)
    
    print(f'#{t} {min_chrg}')