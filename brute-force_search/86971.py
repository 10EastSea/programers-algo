# 전력망을 둘로 나누기
def solution(n, wires):
    answer = n
    
    for cnt in range(len(wires)):
        nodes = [i for i in range(n+1)]
        
        for idx, wire in enumerate(wires):
            if cnt == idx: continue
            
            parent = min(nodes[wire[0]], nodes[wire[1]])
            child = max(nodes[wire[0]], nodes[wire[1]])
            
            # 바뀐 부모 업데이트
            nodes[child], nodes[wire[0]], nodes[wire[1]] = parent, parent, parent
            for i in range(1, n+1):
                if nodes[i] == child or nodes[i] == wire[0] or nodes[i] == wire[1]: nodes[i] = parent
        print(nodes[1:], end="\t")
        
        tower1, tower2 = min(nodes[1:]), max(nodes[1:])
        cnt1, cnt2 = nodes.count(tower1), nodes.count(tower2)
        if answer > abs(cnt1-cnt2): answer = abs(cnt1-cnt2)
        print(cnt1, cnt2, "=>", abs(cnt1-cnt2))
    
    return answer