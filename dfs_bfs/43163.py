# 단어 변환
min_cnt = 51

def comp_str(word1, word2):
    diff_cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]: diff_cnt += 1
    return diff_cnt

def dfs(graph, begin, target, cnt, visited):
    global min_cnt
    
    if begin == target:
        if min_cnt > cnt: min_cnt = cnt
        # print(cnt)
        return
    
    if not visited[begin]:
        visited[begin] = True
        for node in graph[begin]: dfs(graph, node, target, cnt+1, visited)

def solution(begin, target, words):
    answer = 0
    
    graph = {begin: []}
    for word1 in words:
        if comp_str(begin, word1) == 1: graph[begin].append(word1)
        
        graph[word1] = []
        for word2 in words:
            if word1 == word2: continue
            if comp_str(word1, word2) == 1: graph[word1].append(word2)
    # print(graph)
    
    visited = {}
    for key in graph.keys(): visited[key] = False
    dfs(graph, begin, target, 0, visited)
    # print(min_cnt)
    
    if min_cnt <= 50: answer = min_cnt
    return answer