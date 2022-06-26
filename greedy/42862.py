# 체육복
def solution(n, lost, reserve):
    answer = 0

    for i in range(1, n+1):
        if i in lost:
            if i in reserve:
                reserve.remove(i)
                answer += 1
            elif i-1 in reserve:
                reserve.remove(i-1)
                answer += 1
            elif i+1 in reserve:
                if i+1 in lost: continue
                reserve.remove(i+1)
                answer += 1
        else: answer += 1

    return answer