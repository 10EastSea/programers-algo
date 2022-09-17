# 피로도
from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    idx_list = list(range(0, len(dungeons)))
    combs = list(permutations(idx_list, len(dungeons)))
    
    for comb in combs:
        tmp_answer, tmp_k = 0, k
        for i in comb:
            if tmp_k >= dungeons[i][0]: tmp_k -= dungeons[i][1]; tmp_answer += 1
        # print(comb, tmp_answer)
        if answer < tmp_answer: answer = tmp_answer
    
    return answer