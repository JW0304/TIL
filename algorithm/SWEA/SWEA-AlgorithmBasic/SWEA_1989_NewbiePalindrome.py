# 2025-03-02
# 오후 2:02-2:28
# 검토까지 2:51
# SWEA 1989 초심자의 회문검사

import sys
sys.stdin = open('input_1989.txt')

T = int(input())
for t in range(1, T + 1):
    
    # input()으로 문자열로만 받아도 됨!
    word = input()

    # 단어의 길이
    N = len(word)
    
    
    # 1. 처음에 푼 방법 (단어의 길이가 홀수/짝수)
    # # 단어의 길이가 홀수일 때
    # if N % 2 == 1:
    #     # 단어의 길이(N)/2 + 1까지 양쪽이 맞는지 확인
    #     for i in range(N//2 +1):
    #         # 길이가 5면 인덱스 0, 1 과 4, 3이 만나야 함
    #         if word[i] == word[(N-1) - i]:
    #             result = 1
    #         else:
    #             result = 0
    #             break
            
    # # 단어의 길이가 짝수일 때 (예: abba)
    # if N % 2 == 0:
    #     # 단어의 길이(N)/2 까지 양쪽이 맞는지 확인
    #     for i in range(N//2):
    #         # 길이가 4면 0, 1과 3, 2가 만나야 함
    #         if word[i] == word[(N-1) - i]:
    #             result = 1
    #         else:
    #             result = 0
    #             break
        
    # 2. 단어의 길이가 홀수든 짝수든 상관없음
    for i in range(N//2):
        if word[i] == word[(N-1) - i]:
            result = 1
        else:
            result = 0
            break
        
    # 3. 또는 뒤집어도 같은지 확인
    # if word == word[::-1]:
    #     result = 1
    # else:
    #     result = 0
        
    # 맞으면 1을 출력
    # 아니면 0을 출력 (결과값에 1 할당)
    
    print(f'#{t} {result}')