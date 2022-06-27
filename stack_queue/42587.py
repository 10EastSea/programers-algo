# 프린터
def solution(priorities, location):
    answer = 0

    priorities_idx = []
    for i in range(len(priorities)): priorities_idx.append((priorities, i))

    idx = -1
    while location != idx:
        answer += 1

        tmp_idx = priorities.index(max(priorities))
        idx = priorities_idx[tmp_idx][1]

        left1, right1 = priorities[tmp_idx+1:], priorities[:tmp_idx]
        left2, right2 = priorities_idx[tmp_idx+1:], priorities_idx[:tmp_idx]
        priorities = left1 + right1
        priorities_idx = left2 + right2
        # print(idx, priorities)

    return answer