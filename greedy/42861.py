# 섬 연결하기
def solution(n, costs):
    answer = 0
    
    nodes = [i for i in range(n)]
    costs = sorted(costs, key=lambda x: x[2])
    print(nodes); print(costs)
    
    for n1, n2, c in costs:
        if n1 > n2: tmp = n2; n2 = n1; n1 = tmp
        
        p_n1, p_n2 = nodes[n1], nodes[n2]
        while p_n1 != p_n2:
            if p_n2 == nodes[p_n2]: break
            p_n2 = nodes[p_n2]
        if p_n1 != p_n2: answer += c
        
        if p_n1 < nodes[n2]: nodes[nodes[n2]] = p_n1 # 기존에 부모노드가 새로 설정될 부모노드보다 크다면, 기존 노드도 새로운 부모 노드로 세팅
        nodes[n2] = p_n1
    
    return answer