# 순위
def solution(n, results):
    answer = 0

    graph = [[0 for j in range(n+1)] for i in range(n+1)]
    for edge in results: graph[edge[0]][edge[1]] = 1

    # 플로이드-워셜 알고리즘
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][k] + graph[k][j] == 2: graph[i][j] = 1
    
    # 이긴 횟수 + 진 횟수
    answers = [0] * (n+1)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == 1: answers[i] += 1; answers[j] += 1
    
    # 이긴 횟수 + 진 횟수 == n-1 확인 
    for i in range(1, n+1):
        if answers[i] == n-1: answer += 1
    
    return answer