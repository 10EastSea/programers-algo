# 더 맵게
import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    item1 = heapq.heappop(scoville)
    while item1 < K:
        if not scoville:
            answer = -1
            break
        
        item2 = heapq.heappop(scoville)
        new_item = item1 + (item2 * 2)
        heapq.heappush(scoville, new_item)

        item1 = heapq.heappop(scoville)
        answer += 1

    return answer