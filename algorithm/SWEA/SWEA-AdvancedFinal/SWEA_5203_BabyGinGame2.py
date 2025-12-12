import sys
sys.stdin = open('input_5203.txt')

def findwinner(input_list):
    if 3 in input_list:
        return True
    for i in range(8):
        if input_list[i] > 0 and input_list[i + 1] > 0 and input_list[i + 2] > 0:
            return True
    return False

T = int(input())
for t in range(1, T + 1):
    N = 12
    cards = list(map(int, input().split()))

    player1 = [0] * 10
    player2 = [0] * 10
    result = 0

    for n in range(N):
        if n % 2 == 0:
            player1[cards[n]] += 1
            if findwinner(player1):
                result = 1
        else:
            player2[cards[n]] += 1
            if findwinner(player2):
                result = 2
        
        if result != 0:
            break
    

    print(f'#{t} {result}')