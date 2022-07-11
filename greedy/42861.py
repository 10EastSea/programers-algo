# 섬 연결하기
def solution(n, costs):
    answer = 0
    
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for n1, n2, c in costs:
        graph[n1][n2] = c
        graph[n2][n1] = c
    print(graph)
    
    return answer