# 2025-03-03
# 오후 5:35 - 6:22 억지로 풀었음
# 오후 6:29 - 8:09, 저녁 먹고 옴 나중에 제대로 풀자
# 오후 8:10 - 8:25, 마저 풂! 굿
# SWEA 4834

'''
나중에 딕셔너리로 푸는 법도 한 번 보기!
'''

import sys
sys.stdin = open('input_4834.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    input_numbers = list(map(int, input().strip()))
    
    # 0부터 9까지의 숫자를 넣는다 (총 10개)
    range_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    count_numbers = [0] * 10
    
    # 숫자카드를 순회
    # 0 1 2 7 8
    
    # 0, 1, 2, ...9
    for n in range(10):
        # 0, 1, 2, 7, 8
        for i in range(len(input_numbers)):
            if input_numbers[i] == n:
               count_numbers[n] += 1
    
    # ++ 카운트한 값을 순회하며 최대값으로 갱신!!
    # ++ 처음의 값을 최대값이라고 가정 (초기화)
    max_card = count_numbers[0]
    # 해당하는 카드의 번호
    num_card = 0
    for j in range(10):
        if max_card <= count_numbers[j]:
            max_card = count_numbers[j]
            num_card = j
    
    print(f'#{t} {num_card} {max_card}')

# T = int(input())
# for t in range(1, T + 1):
#     # 카드 N장
#     N = int(input())
#     # 0부터 9까지의 숫자 ai가 N장만큼 주어짐
#     # 숫자들을 리스트에 넣기
#     numbers = list(map(int, input().strip()))
    
#     # 숫자와 카드의 장수를 쌍으로 하는 딕셔너리
#     # num_dict = {
#     #     0: 0,
#     #     1: 0,
#     #     2: 0,
#     #     3: 0,
#     #     4: 0,
#     #     5: 0,
#     #     6: 0,
#     #     7: 0,
#     #     8: 0,
#     #     9: 0,
#     # }
    
#     # 딕셔너리에 카드의 장수를 더한다
    
#     # 각 숫자들을 세는 count를 만든다
#     count_0 = 0
#     count_1 = 0
#     count_2 = 0
#     count_3 = 0
#     count_4 = 0
#     count_5 = 0
#     count_6 = 0
#     count_7 = 0
#     count_8 = 0
#     count_9 = 0
    
#     # 카드의 숫자 초기화
#     card_num = 0
    
#     # 총 카드의 수 초기화
#     max_card = 0
    
#     # 리스트를 순회하면서 카운트를 더한다
#     for i in range(len(numbers)):
#         if numbers[i] == 0:
#             count_0 += 1
#             # 최대치보다 클 경우
#             if count_0 >= max_card:
#                 max_card = count_0
#                 # 최대치를 가진 카드 번호 갱신
#                 if card_num <= numbers[i]:
#                     card_num = numbers[i]
#         if numbers[i] == 1:
#             count_1 += 1
#             # 최대치보다 클 경우
#             if count_1 >= max_card:
#                 max_card = count_1
#                 # 최대치를 가진 카드 번호 갱신
#                 if card_num <= numbers[i]:
#                     card_num = numbers[i]
#         if numbers[i] == 2:
#             count_2 += 1
#             # 최대치보다 클 경우
#             if count_2 >= max_card:
#                 max_card = count_2
#                 # 최대치를 가진 카드 번호 갱신
#                 if card_num <= numbers[i]:
#                     card_num = numbers[i]
#         if numbers[i] == 3:
#             count_3 += 1
#             # 최대치보다 클 경우
#             if count_3 >= max_card:
#                 max_card = count_3
#                 # 최대치를 가진 카드 번호 갱신
#                 if card_num <= numbers[i]:
#                     card_num = numbers[i]
#         if numbers[i] == 4:
#             count_4 += 1
#             # 최대치보다 클 경우
#             if count_4 >= max_card:
#                 max_card = count_4
#                 # 최대치를 가진 카드 번호 갱신
#                 if card_num <= numbers[i]:
#                     card_num = numbers[i]
#         if numbers[i] == 5:
#             count_5 += 1
#             # 최대치보다 클 경우
#             if count_5 >= max_card:
#                 max_card = count_5
#                 # 최대치를 가진 카드 번호 갱신
#                 if card_num <= numbers[i]:
#                     card_num = numbers[i]
#         if numbers[i] == 6:
#             count_6 += 1
#             # 최대치보다 클 경우
#             if count_6 >= max_card:
#                 max_card = count_6
#                 # 최대치를 가진 카드 번호 갱신
#                 if card_num <= numbers[i]:
#                     card_num = numbers[i]
#         if numbers[i] == 7:
#             count_7 += 1
#             # 최대치보다 클 경우
#             if count_7 >= max_card:
#                 max_card = count_7
#                 # 최대치를 가진 카드 번호 갱신
#                 if card_num <= numbers[i]:
#                     card_num = numbers[i]
#         if numbers[i] == 8:
#             count_8 += 1
#             # 최대치보다 클 경우
#             if count_8 >= max_card:
#                 max_card = count_8
#                 # 최대치를 가진 카드 번호 갱신
#                 if card_num <= numbers[i]:
#                     card_num = numbers[i]
#         if numbers[i] == 9:
#             count_9 += 1
#             # 최대치보다 클 경우 최대지 갱신
#             if count_9 >= max_card:
#                 max_card = count_9
#                 # 최대치를 가진 카드 번호 갱신
#                 if card_num <= numbers[i]:
#                     card_num = numbers[i]
    
#     # 숫자가 같을 때는 더 큰 수를 출력한다
        
#     print(f'#{t} {card_num} {max_card}')