# 여행경로
from collections import defaultdict

travel_route = []

def dfs(graph, start, visited):
    global travel_route
    travel_route.append(start)
    
    for airport in graph[start]:
        if not airport in visited[start]:
            visited[start].append(airport)
            dfs(graph, airport, visited)
            break

def solution(tickets):
    answer = []
    
    graph = defaultdict(list)
    for ticket in tickets:
        start, end = ticket
        graph[start].append(end)
    for _, value in graph.items(): value.sort()
    # print(graph)
    
    visited = defaultdict(list)
    dfs(graph, "ICN", visited)
    answer = travel_route
    
    return answer