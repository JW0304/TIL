import sys
sys.stdin = open('input_5178.txt')

T = int(input())  # 테스트 케이스 개수 입력

for t in range(1, T + 1):
    # 노드 수 N, 리프 노드 수 M, 값을 출력할 노드 번호 L
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1) 

    for _ in range(M):
        # 리프 노드의 번호, 저장값
        num, store = map(int, input().split())  
        tree[num] = store

    # 부모 노드의 저장값 구하기
    for i in range(N - M, 0, -1):
        c1 = 2 * i 
        c2 = 2 * i + 1  
        if c1 <= N and c2 <= N:
            tree[i] = tree[c1] + tree[c2] 
        else:
            tree[i] = tree[c1] 
    
    print(f'#{t} {tree[L]}')