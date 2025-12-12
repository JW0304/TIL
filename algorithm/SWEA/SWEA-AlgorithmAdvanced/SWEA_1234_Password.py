# 2025-03-11
# 오전 11:57
# SWEA 1234 비밀번호

import sys
sys.stdin = open('input_1234.txt')

T = 10
for t in range(1, T + 1):
    # 문자열의 길이 N, 원래의 비밀번호
    N, original_password = input().split()

    password = str()
    for i in range(int(N)):  # 범위는 문자열 안 됨, 숫자나 리스트는 가능
        password += original_password[i]
        # 문자 하나마다 검사
        if len(password) >= 2 and password[-2] == password[-1]:
            password = password[:-2]

    print(f'#{t} {password}')