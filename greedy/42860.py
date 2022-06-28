# 조이스틱
def solution(name):
    answer = 0

    min_moving = len(name) - 1 # 오른쪽으로 쭉 가면서 바꾸는 경우
    for idx, alpha in enumerate(name):
        # 문자 변경
        answer += min(ord(alpha)-ord('A'), ord('Z')-ord(alpha)+1)

        # A를 만났을 때, 뒤(왼쪽)로 돌아가는 방법 계산하기 위함
        next_idx = idx + 1
        while next_idx < len(name) and name[next_idx] == 'A': next_idx += 1

        # 1. 현재 경우, 2. 현재까지 이동 거리 + 왼쪽으로 돌아간 경우, 3. 왼쪽으로 돌아갔다가 다시 오른쪽으로 이동
        min_moving = min(min_moving, idx + (idx + len(name)-next_idx), idx + 2*(len(name)-next_idx))
    
    answer += min_moving # 변경하는데 필요한 커서 무빙 횟수(answer) + 이동하는데 필요한 커서 무빙 횟수(min_moving)
    return answer


#import heapq

# def solution(name):
#     answer = 0
#     joystick = list("OPQRSTUVWXYZABCDEFGHIJKLMN")

#     name, result = list(name), ['A']*len(name)
#     idx = 0 # 현재 위치
#     while result != name:
#         # 커서 위치 세팅
#         candidates = [] # (이동하는데 필요한 커서 무빙 횟수, 해당 위치)
#         for i in range(len(name)):
#             if name[i] != result[i]:
#                 moving_count = min([(len(name)+(i-idx))%len(name), (len(name)+(idx-i))%len(name)])
#                 heapq.heappush(candidates, (moving_count, i))
#         print(candidates)
#         moving_count, i = heapq.heappop(candidates)
#         answer += moving_count; idx = i

#         # 문자 변경
#         if name[idx] <= 'N': answer += (joystick.index(name[idx]) - joystick.index('A'))
#         else: answer += (joystick.index('A') - joystick.index(name[idx]))
#         result[idx] = name[idx]

#     return answer