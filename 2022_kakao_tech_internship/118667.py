# 두 큐 합 같게 만들기
from collections import deque

def solution(queue1, queue2):
    answer = -1
    
    que1_sum, que2_sum = sum(queue1), sum(queue2)
    if((que1_sum + que2_sum) % 2 != 0): return -1 # 2로 나누었을 때, 나머지가 있으면 나눌 수 없음

    check, cnt = True, 0
    que1, que2 = deque(queue1), deque(queue2)
    while que1_sum != que2_sum:
        if que1_sum > que2_sum:
            num = que1.popleft()
            que1_sum -= num
            que2_sum += num
            que2.append(num)
        elif que1_sum < que2_sum:
            num = que2.popleft()
            que1_sum += num
            que2_sum -= num
            que1.append(num)
        cnt += 1
        
        if cnt > (len(queue1) + len(queue2))*2:
            check = False
            break
            
    if check: answer = cnt
    return answer