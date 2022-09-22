# 두 큐 합 같게 만들기
def solution(queue1, queue2):
    answer = -1
    
    que = queue1 + queue2
    if(len(que) % 2 != 0): return -1 # 2로 나누었을 때, 나머지가 있으면 나눌 수 없음
    half = sum(que) / 2
    
    check, min_cnt = False,2000000000
    for i in range(len(que)):
        tmp_sum = 0
        for j in range(i, len(que)):
            tmp_sum += que[j]
            if tmp_sum == half:
                # print(i, j, que[:i], que[i:j+1], que[j+1:])
                cnt = 0
                
                ## 1. [..i..j..] + [..]
                if j < len(queue1):
                    cnt += j+1             # que1 -> que2
                    cnt += len(queue2) + i # que2 -> que1
                    
                ## 2. [..i..] + [..j..]
                elif i < len(queue1) and j >= len(queue1):
                    cnt += j+1-len(queue1) # que2 -> que1
                    cnt += i               # que1 -> que2
                    
                ## 3. [..] + [..i..j..]
                elif i >= len(queue1):
                    cnt += j+1-len(queue1)   # que2 -> que1
                    cnt += i
                    
                check, min_cnt = True, min(min_cnt, cnt)
                break
                
    if check: answer = min_cnt
    else: answer = -1
    
    return answer