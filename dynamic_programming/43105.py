# 정수 삼각형
def solution(triangle):
    answer = 0

    result = []
    for floor in triangle:
        if not result: result = [floor[0]]; continue
        
        leftist, rightist = result[0]+floor[0], result[-1]+floor[-1]
        tmp_resultist = []
        for i in range(1, len(floor)-1):
            tmp_resultist.append(max(result[i-1]+floor[i], result[i]+floor[i]))
        
        result = [leftist] + tmp_resultist + [rightist]
    answer = max(result)

    return answer