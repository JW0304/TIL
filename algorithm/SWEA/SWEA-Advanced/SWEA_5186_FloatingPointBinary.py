# 2025-03-16
# 오후 5:34
# SWEA 5186 이진수 2

import sys
sys.stdin = open('input_5186.txt')

# 내 풀이 (복잡)
def binary(number):
    global result_num
    for i in range(1, 13):
        if number >= (1/2) ** i:
            number -= ((1/2) ** i)
            result_num += '1'
        elif number < (1/2) ** i:
            result_num += '0'
        if number == 0:
            break
    if number == 0:
        return result_num
    else:
        return 'overflow'

T = int(input())
for t in range(1, T + 1):
    input_number = float(input())
    
    result_num = ''
    print(f'#{t} {binary(input_number)}')
    
# 다른 풀이 (어렵..)
T = int(input())
for t in range(1, T + 1):
    dec_num = float(input())
    bin_num = ''

    while dec_num != 0:

        if len(bin_num) >= 13:
            bin_num = 'overflow'
            break

        dec_num = dec_num * 2
        bin_num += str(dec_num)[0]
        dec_num = float('0.' + str(dec_num)[2:])

    print(f'#{t} {bin_num}')