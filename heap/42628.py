# 이중우선순위큐
import heapq

def solution(operations):
    answer = []

    insert_cnt, delete_cnt = 0, 0
    min_heap, max_heap = [], []
    deleted_min_heap, deleted_max_heap = [], []

    for operation in operations:
        if operation[0] == 'I': # 삽입
            num = int(operation[2:])
            heapq.heappush(min_heap, (num, num))
            heapq.heappush(max_heap, (-num, num))
            insert_cnt += 1
        elif operation[0] == 'D': # 삭제
            if operation[2] == '-': # 최솟값 삭제
                if min_heap:
                    num = heapq.heappop(min_heap)
                    num = (-num[0], num[1])
                    heapq.heappush(deleted_min_heap, num)
            else: # 최대값 삭제
                if max_heap:
                    num = heapq.heappop(max_heap)
                    num = (-num[0], num[1])
                    heapq.heappush(deleted_max_heap, num)
            delete_cnt += 1

    if insert_cnt <= delete_cnt: answer = [0, 0]
    else:
        while deleted_min_heap:
            num = heapq.heappop(deleted_min_heap)[1]
            if num == max_heap[0][1]: heapq.heappop(max_heap)
        while deleted_max_heap:
            num = heapq.heappop(deleted_max_heap)[1]
            if num == min_heap[0][1]: heapq.heappop(min_heap)
        answer = [heapq.heappop(max_heap)[1], heapq.heappop(min_heap)[1]]

    return answer