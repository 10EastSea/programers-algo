# 등산코스 정하기
from collections import defaultdict
import heapq

def solution(n, paths, gates, summits):
    answer = []
    summits = set(summits)
    
    ## 1. 그래프 만들기
    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))
    # print(graph)
    
    
    ## 2. 다익스트라 전처리
    climb = [10000001 for _ in range(n+1)]
    min_heap = []
    for g in gates:
        for next_node, next_weight in graph[g]: heapq.heappush(min_heap, (next_weight, next_node))
        climb[g] = 0
    # print(climb)
    # print(min_heap)
    
    
    ## 3. 다익스트라
    while min_heap:
        here_weight, here_node = heapq.heappop(min_heap)
        
        if here_weight >= climb[here_node]: continue # 현재 갈 수 있는 weight이 최소 weight보다 클 때
        climb[here_node] = here_weight
        
        if here_node in summits: continue            # 현재 위치가 산봉우리일 때
        
        for next_node, next_weight in graph[here_node]:
            if climb[next_node] <= here_weight: continue
            else: heapq.heappush(min_heap, (max(here_weight, next_weight), next_node))
    # print(climb)
    
    
    ## 4. 결과
    summits = list(summits); summits.sort()
    summit_num, min_intensity = 0, 10000001
    for s in summits:
        if min_intensity > climb[s]: summit_num, min_intensity = s, climb[s]
    answer.extend([summit_num, min_intensity])
    return answer



''' 다익스트라 (2차) '''
# def solution(n, paths, gates, summits):
#     answer = []
#     summits.sort()
    
#     # 그래프 생성
#     graph = defaultdict(list)
#     for i, j, w in paths:
#         graph[i].append((w, j))
#         graph[j].append((w, i))
#     for key, value in graph.items(): value.sort()
#     # print(graph)
    
#     # 다익스트라
#     summit_num, min_intensity = -1, 10000001
#     for g in gates:
#         climb = [10000001 for _ in range(n+1)]
#         climb[g] = 0
#         visited = [0 for _ in range(n+1)]
#         visited[g] = 1
        
#         que = deque([g])
#         while que:
#             here = que.popleft()
#             visited[here] = 1
#             if here in summits: continue
            
#             for weight, next_node in graph[here]:
#                 if climb[next_node] > max(weight, climb[here]): climb[next_node] = max(weight, climb[here])
#                 if visited[next_node] != 1: que.append(next_node)
#         # print(g, climb)
        
#         for s in summits:
#             if min_intensity > climb[s]:
#                 summit_num = s
#                 min_intensity = climb[s]
#     # print(summit_num, min_intensity)

#     answer.append(summit_num)
#     answer.append(min_intensity)
#     return answer



'''' 플로이드 와샬 (1차) '''
# def solution(n, paths, gates, summits):
#     answer = []
#     summits.sort()
    
#     # 그래프 생성
#     graph = [[10000001 for _ in range(n+1)] for _ in range(n+1)]
#     for i in range(n+1): graph[i][i] = 0
#     for i, j, w in paths: graph[i][j], graph[j][i] = w, w
#     # for line in graph: print(line)
    
#     # 플로이드 와샬
#     for k in range(n+1):
#         for i in range(n+1):
#             for j in range(n+1):
#                 if graph[i][j] > max(graph[i][k], graph[k][j]):
#                     graph[i][j] = max(graph[i][k], graph[k][j])
#     # for line in graph: print(line)
    
#     summit_num, min_intensity = -1, 10000001
#     for g in gates:
#         for s in summits:
#             if min_intensity > graph[g][s]:
#                 min_intensity = graph[g][s]
#                 summit_num = s
    
#     answer.append(summit_num)
#     answer.append(min_intensity)
#     return answer



''' 테스트 '''
# print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))