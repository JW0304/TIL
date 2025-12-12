# 2025-03-16
# 오전 5:15
# SWEA 22375 스위치 조작

import sys
sys.stdin = open('SWEA_Advanced/input_22375.txt')

def switch(arr1, arr2, N):
    global count
    if arr1 == arr2:
        return count
    for i in range(N):
        if arr1[i] != arr2[i]:
            count += 1
            for j in range(i, N):
                if arr1[j] == 1:
                    arr1[j] = 0
                else:
                    arr1[j] = 1

T = int(input())
for t in range(1, T + 1):

    N = int(input())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))

    count = 0
    switch(Ai, Bi, N)
    print(f'#{t} {count}')