def solution(players, m, k):
    temp_server = [0] * len(players)
    total_server = [0] * len(players)
    needs_server = [0] * len(players)
    # 시간당 서버 몇 개가 필요한지, needs_server
    
    for i in range(len(players)):
        if players[i] >= m :
            needs_server[i] = players[i] // m
            
            if temp_server[i] < needs_server[i]:
                total_server[i] = needs_server[i] - temp_server[i]
            
                for j in range(i, i+k):
                    #print(j, end=" ")
                    if j < len(players):
                        temp_server[j] += total_server[i]
    
    # print("needs_server:", needs_server)
    # print("temp_server:", temp_server)
    answer = sum(total_server)
    return answer