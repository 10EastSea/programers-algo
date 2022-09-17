# 최소직사각형
def solution(sizes):
    answer = 0
    
    w_max, h_max = 0, 0
    for name_card in sizes:
        if w_max < name_card[0]: w_max = name_card[0]
        if h_max < name_card[1]: h_max = name_card[1]
    # print(w_max, h_max)
    
    if w_max > h_max: # 가로가 더 긴 경우
        h_max = 0
        for name_card in sizes:
            h = min(name_card)
            if h_max < h: h_max = h
    else: # 세로가 더 긴 경우
        w_max = 0
        for name_card in sizes:
            w = min(name_card)
            if w_max < w: w_max = w
    
    answer = w_max * h_max
    return answer