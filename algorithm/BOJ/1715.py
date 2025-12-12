import heapq

N = int(input())
heap = []

for _ in range(N):
    heapq.heappush(heap, int(input()))

total = 0

while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    temp = a + b
    total += temp
    heapq.heappush(heap, temp)

print(total)

# 포인트: 힙큐를 사용해서 가장 작은 수를 더하기

'''
오답노트: 
원래는 정렬해서 앞에서부터 더함,
그러나 파일을 합칠 때마다
매번 새롭게 가장 작은 수 2개를 택해서 더해야 함
'''