import sys
sys.stdin = open('input_5208.txt')

def dfs(n, count):  # 현재 위치, 교환 횟수
    global min_chrg
    
    # 최솟값보다 같거나 크면 셀 필요가 없음
    if count >= min_chrg:
        return
    
    # 도착했을 경우
    if n >= N - 1:
        min_chrg = count
        return
    
    # 현재 위치에서 갈 수 있는 범위, dfs 재귀
    for i in range(1, charger[n] + 1):
        dfs(n + i, count + 1)

T = int(input())
for t in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = arr[0]
    charger = arr[1:]
    min_chrg = N - 1  # 최대 교환횟수
    
    dfs(0, -1)  # 시작 위치에서 -1부터 시작
    
    # 최소 충전횟수 출력
    print(f'#{t} {min_chrg}')