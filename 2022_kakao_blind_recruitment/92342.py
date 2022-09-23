# 양궁대회
from itertools import combinations # 조합
from itertools import combinations_with_replacement # 중복조합
import copy

def score_calc(apeach, ryan):
    apeach_score, ryan_score = 0, 0
    for i in range(len(apeach)):
        if apeach[i] == 0 and ryan[i] == 0: continue
        if apeach[i] >= ryan[i]: apeach_score += (10 - i)
        else: ryan_score += (10 - i)
    return ryan_score - apeach_score

def solution(n, info):
    answer = []
    boards = [i for i in range(len(info))]
    
    ryan_score = 0
    for target_num in range(1, n+1):
        board_combs = list(combinations(boards, target_num))
        for board_comb in board_combs:
            board_comb = list(board_comb)
            
            arrows = n
            tmp_result = [0 for _ in range(len(info))]
            
            ## 1. 화살 과녁당 하나씩 할당
            for board in board_comb:
                tmp_result[board] = 1
                arrows -= 1
            
            ## 2. 남은 화살 중복조합으로 할당
            rest_combs = list(combinations_with_replacement(board_comb, arrows))
            for rest_comb in rest_combs:
                result = copy.deepcopy(tmp_result)
                for board in list(rest_comb): result[board] += 1
                
                ## 3. 점수 계산
                tmp_ryan_score = score_calc(info, result)
                if ryan_score < tmp_ryan_score:
                    answer = result
                    ryan_score = tmp_ryan_score
                elif ryan_score == tmp_ryan_score:
                    if ''.join(list(map(str, answer)))[::-1] < ''.join(list(map(str, result)))[::-1]:
                        answer = result
                        ryan_score = tmp_ryan_score
    
    if ryan_score <= 0: answer = [-1]
    return answer