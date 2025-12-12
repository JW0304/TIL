import sys
sys.stdin = open('input_babygin.txt')

T = int(input())
for t in range(1, T + 1):
    cards = list(map(int, input().strip()))
    cards.sort()
    result = False

    # 1. 여섯 숫자가 동일 (aaaaaa)
    if cards[0] == cards[5]:
        result = True

    # 2. 세 숫자씩 동일 (aaabbb)
    if cards[0] == cards[1] == cards[2] and cards[3] == cards[4] == cards[5]:
        result = True

    # 3. 여섯 숫자가 연속 (abcdef)
    i = cards[0]
    if set(cards) == {i, i + 1, i + 2, i + 3, i + 4, i + 5}:
        result = True

    # 4. 두 숫자씩 동일, 연속 2개 (aabbcc)
    if cards[0] == cards[1] and cards[2] == cards[3] and cards[4] == cards[5]:
        if cards[0] == cards[2] - 1 == cards[4] - 2:
            result = True
            
    # 5-1. 앞의 세 숫자가 동일, 뒤의 세 숫자가 연속 (aaabcd)
    if cards[0] == cards[1] == cards[2]:
        if cards[3] == cards[4] - 1 == cards[5] - 2:
            result = True
            
    # 5-2. 앞의 세 숫자가 연속, 뒤의 세 숫자가 동일  (abcddd)
    if cards[0] == cards[1] - 1 == cards[2] -2:
        if cards[3] == cards[4] == cards[5]:
            result = True

    print(f'#{t} {int(result)}')