# 2025-03-01 토
# 오전 11:20 - 12:01
# ~ 오후 3:22
# SWEA 4831 전기버스

'''
한번 충전으로 이동할 수 있는 정류장 수가 정해져 있다
중간에 충전기가 설치된 정류장을 만든다
버스는 0번에서 출발해 종점인 N번 정류장까지 이동한다
한 번 충전으로 최대 이동 가능한 정류장 수는 K이다
충전기가 설치된 M개의 정류장 번호

예시
한 번 충전으로 최대 이동할 수 있는 정류장 K
종점은 N
충전기 설치는 M개

3 10 5
1 3 5 7 9면
1에서 3, 3에서 5,  5에서 7 등등
한 번에 갈 수 있는 거리가 K

단순하게 풀면
인덱스 0과 1, 1과 2, ... N-1과 N
K >= N-(N-1)이어야 함
K < N-(N-1) 이면 못감

range(N)이라고 하면
인덱스 0, 1의 값부터
인덱스 N-1과 N-2의 값까지 계산되어야

하지만... 최소 충전이므로
꼭 충전되지는 않아도 됨

그럼...
다음 충전까지가 K보다 큰지 계산해서
최대치인 곳에서 충전을 하고
그 수를 세어야 할 것 같음

예를 들어
0 + K
K = 3이면
M은 1, 3, 5... 중에
3을 선택

다음으로 3에서 6까지 갈 수 있는데
bus_stop[i] + K
... 5, 7, 9이므로
5를 선택

생략하고
7에서 10까지 갈 수 있는데
bus_stop[i] + K
도착점이 10이므로(N)
10을 선택

선택한 곳 = N이면 끝
카운트를 하나하나 올려야 함

끝

예시에서 충전하는 정류장
1: 3, 5, 7 3개
2: 3, 0 0개
3: 4, 9, 14, ++17 4개

'''
import sys
sys.stdin = open('input_4831.txt')

T = int(input())
for t in range(1, T+1):
    
    # 한번에 갈 수 있는 거리, 총 거리, 정류장의 개수
    K, N, M = map(int, input().split())
    bus_stop = list(map(int, input().split()))
    bus_stop.append(N)

    # ++ 각 테스트케이스마다 초기화
    # 현재 위치를 초기화
    current_location = 0
    # 충전 횟수를 초기화
    charging = 0
    
    # 최소 충전횟수 또는 0을 출력한다
    # 주어진 M을 도착지점에 갈 때까지 순회
    # 리스트의 마지막값이 도착지점
    while current_location != bus_stop[-1]:
        # 버스정류장의 위치들을 리스트에 담기
        # 버스정류장을 이동할 때마다 초기화해야 함
        bus_stop_list = []
        
        # 만약 갈 수 있는 버스정류장이 있다면
        # M의 0, 1, 2... 값 중에 가장 큰 걸 선택
        for i in range(M+1):
            # 갈 수 있는 버스정류장들이 K값보다 작거나 같을때
            # ++ 부등호를 잘못 씀 (K가 더 큰 경우에)
            if bus_stop[i] <= current_location + K:        
                # 갈 수 있는 버스정류장들
                bus_stop_list.append(bus_stop[i])
                
                
        if bus_stop_list[-1] > current_location:    
            # 갈 수 있는 버스정류장들 중 마지막값
            # current_location = bus_stop_list[-1]
            
            # 버스정류장으로 이동했다면 현재위치 다시 설정
            # 그 중에서 현재 위치보다 작은 맥스값
            current_location = max(bus_stop_list)
                
            # 이동할 때마다 충전횟수 +1
            charging += 1
            
        else:
            charging = 0
            break
        
    if charging == 0:
        print(f'#{t} 0')
    else:
    # 도착점에 도착했을 때는 충전하지 않으므로 -1
        print(f'#{t} {charging-1}')