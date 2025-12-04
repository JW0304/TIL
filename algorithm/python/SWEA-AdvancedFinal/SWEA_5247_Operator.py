import sys
sys.stdin = open('input_5247.txt')

from collections import deque

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())

    visited = [0] * (1000000 + 1)
    visited[N] = 1

    # 시작 지점 (시작 숫자, 카운트)
    # 큐를 데크 자료구조로 넣는다 (BFS 탐색)
    queue = deque([(N, 0)])

    # 큐가 비지 않은 동안
    while queue:
        # 큐는 데크이므로 왼쪽에서 뺄 수 있다
        cur, count = queue.popleft()

        if cur == M:
            break
        
        # for문을 통해 BFS
        for next_state in (cur + 1, cur - 1, cur * 2, cur - 10):
            # 범위 지정, 백만 이하의 자연수, 방문했는지 체크
            if 0 <= next_state <= 1000000 and visited[next_state] == 0:
                # 방문 체크
                visited[next_state] = 1
                # 방문 체크하고 다음 상태와 카운트 + 1
                queue.append((next_state, count + 1))

    # 결과 출력
    print(f'#{t} {count}')
