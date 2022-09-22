# 성격 유형 검사하기
def solution(survey, choices):
    answer = ''
    
    score = {"RT": (0,0), "CF": (0,0), "JM": (0,0), "AN": (0,0)}
    for i in range(len(survey)):
        s, c = survey[i], choices[i]
        if s in score: # 정방향 순서 질문
            if c > 4: score[s] = (score[s][0], score[s][1]+(c-4))
            elif c < 4: score[s] = (score[s][0]+(4-c), score[s][1])
        else: # 역방향 순서 질문
            s = s[::-1]
            if c > 4: score[s] = (score[s][0]+(c-4), score[s][1])
            elif c < 4: score[s] = (score[s][0], score[s][1]+(4-c))
    # print(score)
    
    ## 1번 지표
    if score["RT"][0] >= score["RT"][1]: answer += "R"
    elif score["RT"][0] < score["RT"][1]: answer += "T"
    ## 2번 지표
    if score["CF"][0] >= score["CF"][1]: answer += "C"
    elif score["CF"][0] < score["CF"][1]: answer += "F"
    ## 3번 지표
    if score["JM"][0] >= score["JM"][1]: answer += "J"
    elif score["JM"][0] < score["JM"][1]: answer += "M"
    ## 4번 지표
    if score["AN"][0] >= score["AN"][1]: answer += "A"
    elif score["AN"][0] < score["AN"][1]: answer += "N"
    
    return answer