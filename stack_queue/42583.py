# 다리를 지나는 트럭
def solution(bridge_length, weight, truck_weights):
    answer = 0

    on_bridge = [(truck_weights[0], 0)]; del truck_weights[0]
    while truck_weights or on_bridge:
        # 현재 하중
        current_weight = 0
        for truck in on_bridge: current_weight += truck[0]

        # 가능한 트럭 -> 다리 위로
        if truck_weights:
            if current_weight + truck_weights[0] <= weight:
                on_bridge.append((truck_weights[0], 0))
                del truck_weights[0]
        
        # 다리를 건너는 중
        on_bridge = list(map(lambda x: (x[0], x[1]+1), on_bridge))
        # 다리를 지난 트럭 확인
        if on_bridge:
            if on_bridge[0][1] > bridge_length: del on_bridge[0]

        # 현재 하중 다시 계산
        current_weight = 0
        for truck in on_bridge: current_weight += truck[0]

        # 가능한 트럭 -> 다리 위로
        if truck_weights:
            if current_weight + truck_weights[0] <= weight:
                on_bridge.append((truck_weights[0], 1))
                del truck_weights[0]
        
        # print(on_bridge)
        answer += 1

    return answer