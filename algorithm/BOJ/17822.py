import sys
input = sys.stdin.readline

N, M, T = map(int, input().split())

rounds = [list(map(int, input().split())) for _ in range(N)]

for i in range(T):
    x, d, k = map(int, input().split())
    
    # x의 배수인 행
    max = N // x
    for m in range(1, max + 1):
        # N행 중 x * m - 1 번째의 행
        temp_r = x * m - 1
        
        # 시계(가로행 오른쪽으로) / 반시계(가로행 왼쪽으로)
        if d == 0:
            rounds[temp_r] = rounds[temp_r][-k:] + rounds[temp_r][:-k]
        elif d == 1:
            rounds[temp_r] = rounds[temp_r][k:] + rounds[temp_r][:k]
            
    # 인접 행렬 초기화
    adj = [[0] * M for _ in range(N)]

    # 델타 탐색
    ri = [-1, 1, 0, 0]
    ci = [0, 0, -1, 1]
    
    # 인접 행렬에 표시
    for r in range(N):
        for c in range(M):
            for d in range(4):
                dr = r + ri[d]
                dc = (c + ci[d]) % M
                
                # 0 <= dc < M 는 원형이라 범위 필요없음
                if 0 <= dr < N:
                    if rounds[r][c] != 0:
                        if rounds[r][c] == rounds[dr][dc]:
                            adj[r][c], adj[dr][dc] = 1, 1
    
    adj_sum = sum(map(sum, adj))
    rounds_sum = sum(map(sum, rounds))
    rounds_num = 0
    
    # 수가 남아있지 않은 경우
    if rounds_sum == 0:
        continue
    
    # 수가 남아있는 경우
    else:
        # 인접한 같은 수가 없을 때: 평균 구해서 +1 or -1
        if adj_sum == 0:
            for r in range(N):
                for c in range(M):
                    if rounds[r][c] != 0:
                        rounds_num += 1
            avg = rounds_sum / rounds_num
            
            for r in range(N):
                for c in range(M):
                    if rounds[r][c] == 0:
                        continue
                    
                    if rounds[r][c] < avg:
                        rounds[r][c] += 1
                    elif rounds[r][c] > avg:
                        rounds[r][c] -= 1
                        
        # 인접한 같은 수가 있을 때:
        else:
            for r in range(N):
                for c in range(M):
                    if adj[r][c] == 1:
                        rounds[r][c] = 0
                            
result = sum(map(sum, rounds))    
print(result)
                    
'''
오답노트:
인접한 숫자를 2개, 3개씩 지우는 게 아니라
한꺼번에 모아서 지워야 함

예를 들어
1 3 1
3 3 3
1 3 3
과 같은 경우,
2개, 3개씩 지우면 불완전하게 지워짐

포인트:
나머지 연산자(% M)로 원형을 나타냄
음수값도 나머지는 양수로 나옴

자주 하는 실수:
가로는 N, 세로는 M
c 의 범위는 M까지인데 N이라고 씀
자주 하는 실수니까 값이 다르면 한 번 확인할 것
'''