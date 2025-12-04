'''
0xFF 와 같이 0x를 붙이면 16진수
1 2 3 4 5 6 7 8 9 A B C D E F
'''

import sys
sys.stdin = open('input_5185.txt')

# 1. 내장함수 이용
# T = int(input())
# for t in range(1, T + 1):
#     N, hex_str = input().split()
#     N = int(N)
    
#     bin_str = ''
#     # 각 자리를 16진수 -> 2진수
#     for char in hex_str:
#         dec_str = int(char, 16)
#         bin_str += format(dec_str, '04b')
#     print(f'#{t} {bin_str}')

# 2. 내장함수 이용 X
hex_dict = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
}

def toDec(string):
    global dec_list
    for char in string:
        if char in 'ABCDEF':
            char = hex_dict[char]
        else:
            char = int(char)
        dec_list.append(char)
    return dec_list
    
def toBin(list):
    global total_bin
    for target in list:
        bin_zero = [0, 0, 0, 0]
        for one in range(1, 5):
            if target % 2 == 1:
                bin_zero[- one] = 1
            if int(target)//2 == 1:
                bin_zero[- one - 1] = 1
                break
            if int(target)//2 == 0:
                break
            target = target//2
        total_bin += ''.join(map(str, bin_zero))
    return total_bin

T = int(input())
for t in range(1, T + 1):
    N, hex_str = input().split()
    
    dec_list = []
    total_bin = ''
    dec_str = toDec(hex_str)
    bin_str = toBin(dec_str)

    print(f'#{t} {total_bin}')