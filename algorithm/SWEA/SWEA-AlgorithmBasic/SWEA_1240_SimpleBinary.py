import sys
sys.stdin = open('input_1240.txt')

# Python에서는 1초에 3천만 ~ 4천만번 연산

T = int(input())
for t in range(1, T + 1):
    # 배열의 세로크기, 가로크기
    N, M = map(int, input().split())
    arr = [list(map(int, input().strip())) for _ in range(N)]

    # 0. 문제의 조건
    '''
    각 1자리마다 7개의 비트, 총 7 * 8, 56자리의 암호
    0과 1로 이루어진 1 ~ 9를 나타내는 암호문이 주어짐 (해독하기)
    모든 암호문이 1로 끝나므로 마지막의 1의 자리를 찾아서 56자리의 암호를 가져올 것
    해독한 (홀수 자리의 합 * 3 + 짝수 자리의 합) == 10의 배수 일때 올바른 암호
    즉, 자리수로는 (1, 3, 5, 7번째) * 3 + (2, 4, 6, 8) % 10 == 0
    올바른 암호일 경우 암호의 합을 구함, 올바르지 않을 경우 0을 구함
    '''
   
    # 0. 문자열로 받는다
    # 딕셔너리는 키로 값을 찾는다
    secret_code = {
       '0001101' : 0,
       '0011001' : 1,
       '0010011' : 2,
       '0111101' : 3,
       '0100011' : 4,
       '0110001' : 5,
       '0101111' : 6,
       '0111011' : 7,
       '0110111' : 8,
       '0001011' : 9,
   }
    
    # 1. 암호문을 순회하며 1이 나오는 열을 찾는다
    for r in range(N):
        for c in range(M):
            # 시작하는 열을 찾는다
            if arr[r][c] == 1:
                target_r = r
    
    # 2. 암호문의 시작과 끝을 찾는다
    for c2 in range(1, M + 1):
        # 끝점을 찾는다
        if arr[target_r][-c2] == 1:
            # 마지막 인덱스에서 c2만큼 빼기
            end_c = M - c2
            # 찾으면 끝의 1에서 -55 인덱스를 한다
            start_c = end_c - 55
            break
    
    # 3. 찾은 인덱스부터 암호를 변환한다
    # 7개씩 총 8개의 암호
    # start_c부터 + 0, 7, 14, ... 49가 암호문의 시작점
    # 거기에 + 0, 1, 2, ... 6 (start_c가 0이라 하면 인덱스 0부터 55)
    
    # 하나의 테스트케이스마다 리셋
    total_code = []
    
    for i in range(8):  # 0부터 7까지
        # 하나의 코드마다 리셋
        binary_code = ''.join(map(str, arr[target_r][start_c + (7 * i) : start_c + (7 * i) + 7]))
        num_code = secret_code[binary_code]
        
        # 번호 1~7의 코드를 하나의 암호로 만든다
        total_code.append(num_code)
        
    # 자리수로는 (1, 3, 5, 7번째) * 3 + (2, 4, 6, 8) % 10 == 0
    # 인덱스로는 (0, 2, 4, 6번째) * 3 + (1, 3, 5, 7)
    odd_num = total_code[0:8:2]
    even_num = total_code[1:8:2]
		
		# 4. 올바른 암호인지 아닌지 판별한다
		# 괄호로 묶어주지 않으면 우선순위상 % 10 이 먼저 연산됨
    if (sum(odd_num) * 3 + sum(even_num)) % 10 == 0:
        result = sum(total_code)
    else:
        result = 0

    # 올바른 경우 암호코드의 숫자의 합, 잘못된 경우 0
    print(f'#{t} {result}')