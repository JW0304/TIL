# 2025-03-13
# 오전 11:26
# SWEA 5201 컨테이너 운반

import sys
sys.stdin = open('input_5201.txt')

T = int(input())
for t in range(1, T + 1):
    num_cont, num_truck = map(int, input().split())
    weight_cont = list(map(int, input().split()))
    weight_truck = list(map(int, input().split()))

    '''
    - sort: 기존 리스트 정렬
    - sorted: 정렬된 새로운 리스트를 반환

    list.sort()
    new_list = sorted(list)
    '''

    # 옮길 수 없는 경우 0 출력
    count = 0
    # sort해서 W, T의 최댓값부터 매칭
    weight_cont.sort()
    weight_truck.sort()
    
    # T, W를 역순으로 순회
    while len(weight_truck) != 0 and len(weight_cont) != 0:
        if weight_truck[-1] >= weight_cont[-1]:
            count += weight_cont[-1]
            del(weight_truck[-1], weight_cont[-1])
        else:
            del(weight_cont[-1])

    # if T > W면 count += 화물의 무게
    print(f'#{t} {count}')