# 단속카메라
def solution(routes):
    answer = 0
    
    routes = sorted(routes, key=lambda x: x[1])
    # print(routes)
    
    current_camera_loc = -30001
    for i in range(len(routes)):
        start, end = routes[i]
        
        if start <= current_camera_loc: continue
        else: current_camera_loc = end; answer += 1
    
    return answer