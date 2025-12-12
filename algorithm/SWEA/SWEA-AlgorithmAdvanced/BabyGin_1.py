'''
0~9 사이의 숫자 카드, 임의의 카드 6장
3장의 카드가 연속적인 번호일 때 run
3장의 카드가 동일한 번호일 경우 triplet

6자리의 숫자가 babygin인지 판별하라
'''

import sys
sys.stdin = open('input_babygin.txt')

T = int(input())
for t in range(1, T + 1):
    input_list = list(map(int, input().strip()))

    result = False

    # 같은 수만 6개인 경우 (aaaaaa인 경우)
    for num in input_list:
        if input_list == [num] * 6:
            result = True
            break

    # 같은 수가 3개 있으면 리스트에서 삭제
    for target in input_list:
        if input_list.count(target) < 3:
            continue
        else:
            input_list = list(set(input_list) - ({target, target, target}))
            break
    
    # 새로운 리스트가 같은 수가 3개 있는 경우 (aaabbb인 경우)
    for j in input_list:
        if set(input_list) == {j, j, j}:
            result = True
            break
        else:
            break

    # 새로운 리스트가 연속된 수인 경우, 또는 연속된 수만 있는 경우 (abcddd 또는 aabbcc)
    for i in input_list:
        if set(input_list) == {i, i + 1, i + 2}:
            result = True
            break
        elif set(input_list) == {i, i, i + 1, i + 1, i + 2, i + 2}:
            result = True
            break
        elif set(input_list) == {i, i + 1, i + 2, i + 3, i + 4, i + 5}:
            result = True
            break

    print(f'#{t} {int(result)}')