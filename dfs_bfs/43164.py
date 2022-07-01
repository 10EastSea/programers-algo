# 여행경로
from collections import defaultdict

# 해답 참고함..
def solution(tickets):
    answer = []
    
    graph = defaultdict(list)
    for ticket in tickets:
        start, end = ticket
        graph[start].append(end)
    for _, value in graph.items(): value.sort(reverse=True) # 그래프내에 내림차순으로 정렬
    
    stack = ["ICN"]
    while stack:
        here = stack[-1]
        if not graph[here]: answer.append(stack.pop()) # 여기서 방문할 곳이 없다면, 여기는 맨 마지막에 가야함 (정답에 미리 붙임)
        else: stack.append(graph[here].pop()) # 여기서 방문할 곳이 있다면, 지금 방문 (스택에 저장)
    answer.reverse()
    
    return answer


# travel_route = []

# def dfs(graph, start, visited):
#     global travel_route
#     travel_route.append(start)
    
#     for airport in graph[start]:
#         if not airport in visited[start]:
#             visited[start].append(airport)
#             dfs(graph, airport, visited)
#             # break

# def solution(tickets):
#     answer = []
    
#     graph = defaultdict(list)
#     for ticket in tickets:
#         start, end = ticket
#         graph[start].append(end)
#     for _, value in graph.items(): value.sort()
#     # print(graph)
    
#     visited = defaultdict(list)
#     dfs(graph, "ICN", visited)
#     answer = travel_route
    
#     return answer