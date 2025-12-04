# 2025-03-02
# 오전 11:45 - 오후 1:12
# 검토까지 오후 1:27
# SWEA 1209 sum

'''
100x100의 배열
각 행의 합, 각 열의 합, 두 대각선의 합 중 최댓값
'''

import sys
sys.stdin = open('input_1209.txt')

T = 10
for t in range(1, T+1):
    tc = int(input())
    input_arr = [list(map(int, input().split())) for _ in range(100)]
    
    # 행의 합 초기화
    row_sum = [0]
    max_row_sum = 0
        
    # 행의 합 1
    # 행의 합을 100줄까지 구하기
    for r in range(100):
        
        # # sum을 이용해서 풀기
        # # sum(input_arr[r])
        # one_row_sum = 0
        # one_row_sum += sum(input_arr[r])
        
        # # 비교한 것 중 큰 것을 남긴다
        #    # 한 줄마다 비교해서 넣기
        # if max_row_sum < one_row_sum:
        #     max_row_sum = one_row_sum
        
        # r이 0이 아닌 1보다 클 때, 자기보다 하나 작은 수를 더함
        # if r >= 1:
        #     # 오른쪽의 값이 더 크면
        #     if sum(input_arr[r]) > sum(input_arr[r-1]):
        #         row_sum.append(sum(input_arr[r]))
        #     else:
        #         row_sum.append(sum(input_arr[r-1]))
        # # r = 0인  경우도 더해줘야 함
        # else:
        #     row_sum.append(sum(input_arr[r]))
    # # 모든 연산이 끝나면 하나의 최고값을 구한다
    # row_sum.sort(reverse=True)
    # max_row_sum = row_sum[0]
        
        if max_row_sum < sum(input_arr[r]):
            max_row_sum = sum(input_arr[r])
                                
    # 행의 합 2  
    # 가우스의 식을 이용해서 행의 합을 구하기
    # 0과 99, 1과 98... 9와 90, ... 49와 50
    # input_arr[r][i]에서 i(99-i)
    # 생각해보니 합의 평균이 아니므로 그냥 0부터 i의 합을 구하면 됨
    
    # 2중 for문이라 너무 비효율적임
    # one_row_sum = 0
    # for r in range(50):
    #     for i in range(100):
    #         one_row_sum += input_arr[r][i]
    #     row_sum.append(one_row_sum)
    
    # # 정렬해서 최고값을 구한다
    # row_sum.sort()
    # max_row_sum = row_sum[-1]
    
    # 열의 합을 100줄까지 구하면서
    # 열의 합은 각각 다른 행에서 같은 열을 더한 것
    # input[0][1], input[0][2]... 를 더한 값
    # ++ 이 아니라 input[1][0], input[2][0] ... 을 더한 값!!!
    
    # ++ 아래는 가로의 합!!!
    # max_col_sum = 0
    # for r in range(100):
    #     one_col_sum = 0
    #     for c in range(100):
    #         one_col_sum += input_arr[r][c]
    
    # ++ 아래가 세로의 합!!!
    # ++ r과 c의 순서가 바뀌어야 함!!!
    max_col_sum = 0
    for c in range(100):
        one_col_sum = 0
        for r in range(100):
            one_col_sum += input_arr[r][c]
            
        # 한 줄마다 비교해서 넣기
        if max_col_sum < one_col_sum:
            max_col_sum = one_col_sum
            

    # 위에서 한줄마다 비교했으므로 필요없음
    # 정렬해서 최고값을 구한다
    # col_sum.sort()
    # max_col_sum = col_sum[-1]
    
    # 대각선 diagonal
    # \ 방향 대각선의 합을 구한다
    downward_dia_sum = 0
    # (0, 0) 부터 (99, 99)까지의 합
    for i in range(100):
        downward_dia_sum += input_arr[i][i]
    
    # / 방향 대각선의 합을 구한다
    upward_dia_sum = 0
    # (99, 0) 부터 (0, 99)까지의 합
    for j in range(100):
        upward_dia_sum += input_arr[99-j][j]
    
    # 네 합을 총 합의 리스트로 구한다
    # total_max_value = []
    # total_max_value.append(max_row_sum)
    # total_max_value.append(max_col_sum)
    # total_max_value.append(downward_dia_sum)
    # total_max_value.append(upward_dia_sum)
    
    # 각 값을 append 말고 변수로 넣어줘도 됨
    total_max_value = [max_row_sum, max_col_sum, downward_dia_sum, upward_dia_sum]
    
    # 네개를 정렬한 후 -1의 값을 구한다
    total_max_value.sort()
    max_value = total_max_value[-1]
    
    print(f'#{t} {max_value}')