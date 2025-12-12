# 2025-03-11
# 오후 12:24
# SWEA 5356 의석이의 세로로 말해요

import sys
sys.stdin = open('input_5356.txt')

T = int(input())
for t in range(1, T + 1):
    chars = [input() for _ in range(5)]

    final_chars = str()  # 출력할 글자
    for j in range(15):
        for i in range(5):
            # try, except: 시도해보고 없으면 건너뛰기
            try:
                if chars[i][j]:
                    final_chars += chars[i][j]
            except:
                continue

    print(f'#{t} {final_chars}')