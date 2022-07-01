# 구명보트
from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    
    deq = deque(people)
    while deq:
        if len(deq) == 1: answer += 1; break
        elif deq[0] + deq[-1] <= limit:
            deq.popleft(); deq.pop(); answer += 1
        else: deq.pop(); answer += 1
    
    return answer


# def solution(people, limit):
#     answer = 0
#     people.sort(reverse=True)
    
#     boats = []
#     for p in people:
#         check = False
#         for i in range(len(boats)):
#             if boats[i] + p <= limit:
#                 boats[i] = limit + 1
#                 answer += 1; check = True; break
#         if not check: boats.append(p)
    
#     for b in boats:
#         if b <= limit: answer += 1
    
#     return answer