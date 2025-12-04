# 2025-03-18
# 오후 12:24
# SWEA 5208 전기버스2

import sys
sys.stdin = open('input_5208.txt')

'''
어렵 ㅠ
'''

def travel(temp_location):
    global count
    global min_battery_swap

    if count >= min_battery_swap:
        return
    
    if temp_location + bus_stop[temp_location] >= N - 1:
        min_battery_swap = min(min_battery_swap, count)
        return
    
    for i in range(1, bus_stop[temp_location] + 1):
        count += 1
        travel(temp_location + i)
        count -= 1  # 백트래킹 (재귀 호출 후 count 복원)

T = int(input())
for t in range(1, T + 1):
    # N개의 정류장, N-1개의 정류장별 배터리 용량, 종점의 배터리는 0
    input_date = list(map(int, input().split()))
    N = input_date[0]
    bus_stop = input_date[1:] + [0]

    # 최소 교환횟수
    min_battery_swap = N
    count = 0
    travel(0)

    print(f'#{t} {min_battery_swap}')