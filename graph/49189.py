# 가장 먼 노드
def solution(n, edge):
    answer = 0

    graph = {} # 양방향 그래프
    for i in range(1, n+1): graph[i] = []
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    # print(graph)

    queue = [(1, 0)] # 왼쪽: node, 오른쪽: level
    visited = [-1] * (n+1)
    visited[1] = 0
    while queue:
        node_level = queue.pop(0)
        node, level = node_level[0], node_level[1]

        for next_node in graph[node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[node] + 1
                queue.append((next_node, level+1))
    answer = visited.count(max(visited))
    
    return answer