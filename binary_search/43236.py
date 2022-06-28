# 징검다리
def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    
    start, middle, end = rocks[0]-0, [], distance-rocks[-1]
    for i in range(len(rocks)-1):
        middle.append(rocks[i+1]-rocks[i])
    distances = [start] + middle + [end]
    print(distances)

    return answer

# print(solution(25, [2, 14, 11, 21, 17], 2))