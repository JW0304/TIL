# 2025-03-12
# 오후 12:00
# SWEA 5177 이진힙

import sys
sys.stdin = open('input_5177.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    '''
    입력 순서대로 이진 최소힙에 저장, 
    마지막 노드의 조상 노드에 저장된 정수의 합
    '''
    # 자식 노드
    p = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for i in range(1, N//2 + 1):
        left[i] = i * 2
        right[i] = i * 2 + 1

    

    # 자식 노드를 인덱스로 부모를 찾는다

    par[c]

    print(f'#{t} {result}')


# def min_heap(node):
#     parent = node // 2
#     if parent < 1:
#         return
#     if heap[parent] > heap[node]:
#         heap[parent], heap[node] = heap[node], heap[parent]
#         min_heap(parent)

# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     numbers = list(map(int, input().split()))
    
#     heap = [0]
#     for num in numbers:
#         heap.append(num)
#         min_heap(len(heap) - 1)
    
#     result = 0
#     node = len(heap) - 1  # 마지막 노드의 인덱스
#     while node > 0:
#         node //= 2  # 부모 노드로 이동
#         result += heap[node]
    
#     print(f'#{t} {result}')