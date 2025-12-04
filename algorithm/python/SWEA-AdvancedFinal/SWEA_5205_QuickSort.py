import sys
sys.stdin = open('input_5205.txt')

def quicksort(arr, start, end):
    pivotindex = partition(arr, start, end)
    quicksort(arr, start, pivotindex - 1)
    quicksort(arr, pivotindex + 1, end)
    
def partition(arr, start, end):
    pass


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    quicksort(arr, 0, N - 1)
    print(f'#{t} {arr[N//2]}')