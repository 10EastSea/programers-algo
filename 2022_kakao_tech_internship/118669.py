# 등산코스 정하기
from collections import defaultdict
from collections import deque

def solution(n, paths, gates, summits):
    answer = []
    summits.sort()
    
    # 그래프 생성
    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((w, j))
        graph[j].append((w, i))
    for key, value in graph.items(): value.sort()
    # print(graph)
    
    # 다익스트라
    summit_num, min_intensity = -1, 10000001
    for g in gates:
        climb = [10000001 for _ in range(n+1)]
        climb[g] = 0
        visited = [0 for _ in range(n+1)]
        visited[g] = 1
        
        que = deque([g])
        while que:
            here = que.popleft()
            visited[here] = 1
            if here in summits: continue
            
            for weight, next_node in graph[here]:
                if climb[next_node] > max(weight, climb[here]): climb[next_node] = max(weight, climb[here])
                if visited[next_node] != 1: que.append(next_node)
        # print(g, climb)
        
        for s in summits:
            if min_intensity > climb[s]:
                summit_num = s
                min_intensity = climb[s]
    # print(summit_num, min_intensity)

    answer.append(summit_num)
    answer.append(min_intensity)
    return answer


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