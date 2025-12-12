import sys
sys.stdin = open('input_5203.txt')

T = int(input())
for t in range(1, T + 1):
    cards = list(map(int, input().split()))

    pl1 = []
    pl2 = []
    result = 0

    for i in range(12):
        # 나머지가 0일 경우 pl1
        if i % 2 == 0:
            pl1.append(cards[i])
        else:
            pl2.append(cards[i])

        # 카드가 3개 이상인 경우
        if len(pl1) >= 3 or len(pl2) >= 3:

            for j in range(len(pl1)):
                # triplet인지 확인
                if pl1.count(pl1[j]) >= 3:
                    result = 1
                    break
                break

            for k in range(len(pl1)):
                # 리스트를 순회하며 run인지 확인
                pl1.sort()
                if k + 3 <= len(pl1) and pl1[k:k+3] == [pl1[k], pl1[k]+1, pl1[k]+2]:
                    result = 1
                    break
                break
                
            for m in range(len(pl2)):
                # triplet인지 확인
                if pl2.count(pl2[m]) >= 3:
                    result = 2
                    break
                break

            for n in range(len(pl2)):
                # 리스트를 순회하며 run인지 확인
                pl2.sort()
                if n + 3 <= len(pl2) and pl2[n:n+3] == [pl2[n], pl2[n]+1, pl2[n]+2]:
                    result = 2
                    break
                break

    print(f'#{t} {result}')
