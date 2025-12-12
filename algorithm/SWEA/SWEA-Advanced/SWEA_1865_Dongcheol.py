def work(total):
    global staff, max_success

    # 가지치기 (성공률이 최대보다 작거나 같을 경우)
    if total <= max_success:
        return
    
    # 모든 직원에게 작업이 배당된 경우
    if len(staff) == N:
        max_success = max(max_success, total)
        return
    
    # 그렇지 않은 경우
    else:
        for i in range(N):
            # i번째의 일이 배당되지 않았다면
            if i not in staff:
                # 일했다고 더해주기
                staff.append(i)
                # 성공률 곱하기
                work(total * (success[len(staff)-1][staff[-1]] / 100))
                # 백트래킹 (원상복구)
                staff.pop()

T = int(input())
for t in range(1, T+1):
    N = int(input())
    # 직원별 성공률 (N x N)
    success = [list(map(int, input().split())) for _ in range(N)]
    staff = []
    max_success = 0
    work(1)
    # 소수점 6자리까지 출력
    print(f"#{t} {max_success * 100:.6f}")