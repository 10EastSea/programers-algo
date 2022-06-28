# 네트워크
def dfs(graph, computer, visited):
    if visited[computer] == 0: # 방문하지 않았을 때
        visited[computer] = 1
        for connected_computer in graph[computer]: dfs(graph, connected_computer, visited)

def solution(n, computers):
    answer = 0

    graph = {i: [] for i in range(n)}
    for a_computer, a_connected in enumerate(computers):
        for b_computer, b_is_connected in enumerate(a_connected):
            if b_is_connected == 1 and b_computer != a_computer:
                graph[a_computer].append(b_computer)
    print(graph)

    visited = [0]*n
    for computer in range(n):
        if visited[computer] == 0:
            dfs(graph, computer, visited)
            answer += 1

    return answer