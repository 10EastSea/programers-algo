# 섬 연결하기
def solution(n, costs):
    answer = 0
    
    nodes = [i for i in range(n)]
    costs = sorted(costs, key=lambda x: x[2])
    # print(nodes); print(costs)
    
    for n1, n2, c in costs:
        p_n1, p_n2 = nodes[n1], nodes[n2]
        if p_n1 > p_n2: # p_n1이 더 작은 값이 되도록 세팅
            tmp = p_n2; p_n2 = p_n1; p_n1 = tmp
            tmp = n2; n2 = n1; n1 = tmp
        
        while p_n1 != p_n2: # 두 부모가 같지 않을때, 혹시 n2의 진짜 부모가 다를 수도 있으니 n2의 진짜 부모 찾음
            if p_n2 == nodes[p_n2]: break
            p_n2 = nodes[p_n2]
        if p_n1 != p_n2: answer += c # 그래도 같지 않다면, 두 노드는 연결되어 있지 않음 -> 연결
        
        tmp = nodes[n2] # 기존 n2에 세팅된 부모로 가지고 있는 모든 노드들에게 새로운 부모 노드를 세팅
        for i in range(n):
            if nodes[i] == tmp: nodes[i] = p_n1
            
    return answer