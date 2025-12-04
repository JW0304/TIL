# 2025-03-11
# 오후 12:53
# SWEA 2115 벌꿀채취

'''
주석을 달며 풀어서 풀이하고
나중에 최적화 (함수 등)
'''

import sys
import itertools
sys.stdin = open('input_2115.txt')

T = int(input())
for t in range(1, T + 1):
    # 크기 N, 가로 길이 M, 한계치 C
    N, M, C = map(int, input().split())
    beehive = [list(map(int, input().split())) for _ in range(N)]
    max_revenue = 0

    # 첫번째 일꾼
    for worker1_i in range(N):
        for worker1_j in range(N - M + 1):
            worker1_range = beehive[worker1_i][worker1_j : worker1_j + M]


            # 부분집합의 최댓값을 구한다 (M = 3이라면, 부분집합은 3C1 + 3C2 + 3C3)
            worker1_max = 0
            for elements_num in range(1, M + 1):
                subset = itertools.combinations(worker1_range, elements_num)

                for one_subset in subset:
                    if sum(one_subset) > C:
                        continue
                    
                    # 각 부분집합의 원소들을 제곱한 합
                    one_subset_sum = 0
                    for one_subset_elements in one_subset:
                        one_subset_sum += (one_subset_elements ** 2)

                    # 각 부분집합의 합, 첫번째 일꾼의 최대값 비교
                    if worker1_max <= one_subset_sum:
                        worker1_max = one_subset_sum
            
            # 두번째 일꾼
            for worker2_i in range(worker1_i, N):
                for worker2_j in range(N - M + 1):
                    if worker1_i == worker2_i and worker1_j < worker2_j + M:
                        continue
                    worker2_range = beehive[worker2_i][worker2_j : worker2_j + M]


                    # 부분집합의 최댓값을 구한다 (M = 3이라면, 부분집합은 3C1 + 3C2 + 3C3)
                    worker2_max = 0
                    for elements_num in range(1, M + 1):
                        subset = itertools.combinations(worker2_range, elements_num)

                        for one_subset in subset:
                            if sum(one_subset) > C:
                                continue

                            one_subset_sum = 0
                            for one_subset_elements in one_subset:
                                one_subset_sum += (one_subset_elements ** 2)

                        # 각 부분집합의 합, 첫번째 일꾼의 최대값 비교
                        if worker2_max <= one_subset_sum:
                            worker2_max = one_subset_sum

                    max_revenue = max(max_revenue, worker1_max, worker2_max)

    print(f'#{t} {max_revenue}')