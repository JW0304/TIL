# 2025-03-16
# 오후 7:39
# SWEA 1240 단순 2진 암호코드

import sys
sys.stdin = open('input_1240.txt')

CODES = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    
    matrix = [list(map(int, input().strip())) for _ in range(N)]
    
    # 뒤에서부터 (M과 암호코드의 길이의 차) + 1까지 탐색
    password = []
    for i in range(N):
        for j in range(1, M - 56 + 1):
            if matrix[i][- j] == 1:
                password = matrix[i][- j + 1 - 56 : - j + 1]
                break
        if password != []:
            break
    
    full_password = str()
    for bits in range(8):
        seven_bits = ''.join(map(str, password[bits * 7 : bits * 7 + 7]))
        partial_password = CODES[seven_bits]
        full_password += str(partial_password)
        
    odd_num = list(full_password[0:8:2].strip())
    even_num = list(full_password[1:8:2].strip())
    if ((sum(map(int, odd_num)) * 3) + sum(map(int, even_num))) % 10 == 0:
         result = sum(list(map(int, full_password.strip())))
    else:
        result = 0
    
    print(f'#{t} {result}')