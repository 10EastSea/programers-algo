# 징검다리
def solution(distance, rocks, n):
    answer = 0
    rocks.sort()

    start, end = 0, distance
    while start <= end:
        middle = (start+end) // 2
        
        remove_count = 0; pre_rock = 0
        for current_rock in rocks:
            if current_rock - pre_rock < middle: remove_count += 1
            else: pre_rock = current_rock
        
        # print(start, middle, end, "/ remove count:", remove_count)
        if remove_count > n: end = middle-1
        else: # remove_count < n
            answer = middle
            start = middle+1
    
    return answer


# def solution(distance, rocks, n):
#     answer = 0
#     rocks.sort()
    
#     start, middle, end = rocks[0]-0, [], distance-rocks[-1]
#     for i in range(len(rocks)-1):
#         middle.append(rocks[i+1]-rocks[i])
#     distances = [start] + middle + [end]
#     print("before", distances)

#     for i in range(n):
#         remove_idx = distances.index(min(distances))
#         if remove_idx == len(distances)-1:
#             distances[remove_idx-1] += distances[remove_idx]
#             del distances[remove_idx]
#         else:
#             distances[remove_idx+1] += distances[remove_idx]
#             del distances[remove_idx]
#     print("after", distances)

#     answer = min(distances)
#     return answer