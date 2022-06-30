# 등굣길
def solution(m, n, puddles):
    answer = 0
    
    path = [[0 for _ in range(m)] for _ in range(n)]
    for puddle in puddles: path[puddle[1]-1][puddle[0]-1] = -1
    
    for i in range(1, len(path)): # 세로축 세팅
        if path[i][0] == -1: break
        else: path[i][0] = 1
    for j in range(1, len(path[0])): # 가로축 세팅
        if path[0][j] == -1: break
        else: path[0][j] = 1
    # print(path)
    
    for i in range(1, len(path)):
        for j in range(1, len(path[i])):
            if path[i][j] == -1: continue
            
            if path[i-1][j] != -1 and path[i][j-1] != -1: path[i][j] = (path[i-1][j] + path[i][j-1]) % 1000000007
            elif path[i-1][j] == -1 and path[i][j-1] != -1: path[i][j] = path[i][j-1] % 1000000007
            elif path[i-1][j] != -1 and path[i][j-1] == -1: path[i][j] = path[i-1][j] % 1000000007
    # print(path)
    
    answer = path[n-1][m-1]
    return answer