# 두 큐 합 같게 만들기
def solution(queue1, queue2):
    answer = -1
    
    que = queue1 + queue2
    if(sum(que) % 2 != 0): return -1 # 2로 나누었을 때, 나머지가 있으면 나눌 수 없음
    half = sum(que) / 2
    
    i, j = 0, 0
    tmp_sum = 0
    check, min_cnt = False, 10000000000
    while j < len(que):
        tmp_sum += que[j]
        # print(i, j, que[:i], que[i:j+1], que[j+1:], tmp_sum)
        
        if tmp_sum < half:
            j += 1
            continue
        
        while tmp_sum > half and i < j:
            tmp_sum -= que[i]
            i += 1
        
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
        
        j += 1
    
    
#     for i in range(len(que)):
#         tmp_sum = 0
#         for j in range(i, len(que)):
#             tmp_sum += que[j]
#             if tmp_sum == half:
#                 # print(i, j, que[:i], que[i:j+1], que[j+1:])
#                 cnt = 0
                
#                 ## 1. [..i..j..] + [..]
#                 if j < len(queue1):
#                     cnt += j+1             # que1 -> que2
#                     cnt += len(queue2) + i # que2 -> que1
                    
#                 ## 2. [..i..] + [..j..]
#                 elif i < len(queue1) and j >= len(queue1):
#                     cnt += j+1-len(queue1) # que2 -> que1
#                     cnt += i               # que1 -> que2
                    
#                 ## 3. [..] + [..i..j..]
#                 elif i >= len(queue1):
#                     cnt += j+1-len(queue1)   # que2 -> que1
#                     cnt += i
                    
#                 check, min_cnt = True, min(min_cnt, cnt)
#                 break
#             elif tmp_sum > half: break
                
    
    if check: answer = min_cnt
    return answer