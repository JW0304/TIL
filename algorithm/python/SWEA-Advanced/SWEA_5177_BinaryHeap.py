# 2025-03-12 -> 15
# 오후 12:00 -> 7:27
# SWEA 5177 이진힙

import sys
sys.stdin = open('input_5177.txt')

def ancestor(node):
    global count
    count += value[parent[node]]
    if parent[node] != 0:
        ancestor(parent[node])
    return count

# 원래는 한 번만 교환 -> 부모 < 자식 될때까지 교환
def swap(cur):
    if parent[cur] != 0:
        if value[parent[cur]] > value[cur]:
            value[parent[cur]], value[cur] = value[cur], value[parent[cur]]
            swap(parent[cur])

T = int(input())
for t in range(1, T + 1):
    V = int(input())
    E = V - 1
    numbers = list(map(int, input().split()))
    
    parent = [0] * (V + 1)
    value = [0] * (V + 1)
    
    for child in range(2, V + 1):
        parent[child] = child//2
    
    # 노드에 순서대로 저장값을 저장
    for i in range(1, V + 1):
        num = numbers[i - 1]
        value[i] = num
        # 최소힙: if 부모 > 자식이면 부모, 자식 = 자식, 노드
        swap(i)
                             
    # 마지막 노드의 조상 노드의 합
    count = 0
    print(f'#{t} {ancestor(V)}')