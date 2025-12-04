# 2025-03-18
# 오전 10:37
# SWEA 5208 전기버스2

import sys
sys.stdin = open('input_5208.txt')

'''
Fail
10개 중 7개 맞음

무조건 큰 수부터 선택 X
작은 수를 택하는 게 최선의 선택일 때도 있음
'''

def travel(temp_location, battery):
    global N
    global count

    if temp_location + battery >= N - 1:
        return count

    if temp_location + battery < N - 1:
        travel_range = bus_stop[temp_location + 1: temp_location + battery + 1]
        max_battery = max(travel_range)

        max_battery_location = temp_location
        for i in range(temp_location + battery, temp_location, -1):
            if bus_stop[i] == max_battery:
                max_battery_location = i
                break
        count += 1

        temp_location = max_battery_location
        battery = max_battery
        return travel(temp_location, battery)

T = int(input())
for t in range(1, T + 1):
    # N개의 정류장, N-1개의 정류장별 배터리 용량
    # 종점의 배터리는 0
    input_date = list(map(int, input().split()))
    N = input_date[0]
    bus_stop = input_date[1:] + [0]

    # 출발지에서 배터리 장착, 최소 교환횟수
    battery = bus_stop[0]
    temp_location = 0
    count = 0
    result = travel(temp_location, battery)

    print(f'#{t} {result}')