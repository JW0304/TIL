# 2025-03-14
# 오후 12:15
# SWEA 1952 수영장

import sys
sys.stdin = open('input_1952.txt')

# T = int(input())
# for t in range(1, T + 1):


#     print(f'#{t} {result}')


if __name__ == "__main__":
    T = int(input())
    for test_case in range(1, T + 1):
        d_fare, m_fare, tm_fare, y_fare = map(int, input().split())

        plan = list(map(int, input().split()))

        # 12월부터 거꾸로 진행 3개월권 계산을 위해 15로 할당
        dp = [0 * 12] * 15
        for month in range(11, -1, -1):
            dp[month] = min(dp[month + 1] + d_fare * plan[month], dp[month + 1] + m_fare, tm_fare + dp[month + 3], y_fare)

        print(f"#{test_case} {dp[0]}")