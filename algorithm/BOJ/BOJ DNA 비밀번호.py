'''
https://www.acmicpc.net/problem/12891

<입력>
문자열의 총 길이 S(int), 부분 문자열의 길이 P(int)
문자열 (String)
A C G T의 최소 개수(int)
'''

import sys
input = sys.stdin.readline

S, P = map(int, input().split())
DNA = input()
A, C, G, T = map(int, input().split())
count = 0

# 맨 처음 부분 문자열의 문자 개수 세기
count_A = DNA[:P].count('A')
count_C = DNA[:P].count('C')
count_G = DNA[:P].count('G')
count_T = DNA[:P].count('T')

# 맨 처음 부분 문자열 체크
if count_A >= A and count_C >= C and count_G >= G and count_T >= T:
    count += 1

# 슬라이딩 윈도우: 한 칸씩 이동, 왼쪽 끝은 빼고(문자 개수 감소) 오른쪽 끝에 추가(문자 개수 추가)
for i in range(1, S - P + 1):
    # 제거되는 문자 (왼쪽 끝)
    remove_char = DNA[i - 1]
    if remove_char == 'A':
        count_A -= 1
    elif remove_char == 'C':
        count_C -= 1
    elif remove_char == 'G':
        count_G -= 1
    elif remove_char == 'T':
        count_T -= 1
    
    # 추가되는 문자 (오른쪽 끝)
    add_char = DNA[i + P - 1]
    if add_char == 'A':
        count_A += 1
    elif add_char == 'C':
        count_C += 1
    elif add_char == 'G':
        count_G += 1
    elif add_char == 'T':
        count_T += 1
    
    # 조건 체크
    if count_A >= A and count_C >= C and count_G >= G and count_T >= T:
        count += 1

print(count)
