import sys
sys.stdin = open('input_quicksort.txt')

def quicksort(arr):
    # pivot을 맨 오른쪽으로 설정
    pivot = arr[-1]
    
    s = 0
    e = -2
    N = len(arr)
    for i in range(N//2):
        if i == N//2:
            if arr[s] >= pivot:
                arr[:s + 1] + arr[-1] + arr[s:]
            
        if arr[s] >= pivot and arr[e] <= pivot:
            arr[s], arr[e] = arr[e], arr[s]
            s += 1
            e -= 1
    

T = int(input())
for t in range(1, T + 1):
    arr = list(map(int, input().split()))
    
    quicksort(arr)
    
    print(f'#{t} {arr}')
    
# ------------------------------------------------
# 예시코드

def quick_sort(arr, start, end):
    """ 퀵 정렬 알고리즘 (재귀적 구현) """
    if start >= end:  # 원소가 하나 이하인 경우 정렬 불필요
        return
    pivot_index = partition(arr, start, end)  # 피벗을 기준으로 분할
    quick_sort(arr, start, pivot_index - 1)  # 왼쪽 부분 정렬
    quick_sort(arr, pivot_index + 1, end)  # 오른쪽 부분 정렬


def partition(arr, start, end):
    """ 배열을 피벗을 기준으로 나누는 함수 """
    pivot = arr[start]  # 첫 번째 요소를 피벗으로 설정
    left = start + 1
    right = end

    while left <= right:
        while left <= right and arr[left] < pivot:  # 피벗보다 큰 값 찾기
            left += 1
        while left <= right and arr[right] > pivot:  # 피벗보다 작은 값 찾기
            right -= 1
        if left <= right:  # left와 right가 교차되지 않았다면 swap
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    arr[start], arr[right] = arr[right], arr[start]  # 피벗을 올바른 위치로 이동

    return right  # 피벗의 최종 위치 반환


T = int(input())  # 테스트 케이스 개수 입력

for case_num in range(1, 1 + T):
    my_arr = list(map(int, input().split()))  # 정렬할 배열 입력
    quick_sort(my_arr, 0, len(my_arr) - 1)  # 퀵 정렬 실행
    print(f"#{case_num} {my_arr}")  # 정렬된 배열 출력