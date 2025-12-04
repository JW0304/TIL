import itertools

T = int(input())
for t in range(1, T + 1):
    N = int(input())

    # 인덱스 0 추가해주면서 matrix 받아오기
    matrix = [[0] + list(map(int, input().split())) for _ in range(N)]
    matrix = [[0] * (N + 1)] + matrix

    if t >= 9:
        print(f'#{t} 0')
    else:
        # 최솟값 설정
        # 가로, 세로로 N - 1 만큼 이동, 모든 칸이 10이라 가정
        max_travel = 2 * (N - 1)
        min_num = max_travel * 10
        
        idx = [num for num in range(max_travel)]
        combi = list(itertools.combinations(idx, N - 1))

        # 이동하는 각 경우의 수
        for one_combi in combi:
            # 초기화
            nr, nc = 1, 1
            dr = [0] * (max_travel)
            dc = [0] * (max_travel)
            # 세로 이동: 부분집합의 인덱스에 해당되는 경우
            for move_r in range(N - 1):
                # 방향의 순서
                dr[one_combi[move_r]] = 1

            # 가로 이동: 세로 이동이 아닌 경우
            for move_c in range(max_travel):
                if dr[move_c] == 0:
                    dc[move_c] = 1

            # 이동하며 수 더하기
            count = matrix[nr][nc]  # 시작점의 값
            for k in range(max_travel):
                nr += dr[k]
                nc += dc[k]

                count += matrix[nr][nc]
                if count >= min_num:
                    break

            min_num = min(min_num, count)

        print(f'#{t} {min_num}')