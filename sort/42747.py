# H-Index
def solution(citations):
    answer = 0
    citations.sort()

    h = 0
    while h <= len(citations):
        h_cnt = 0
        for c in citations:
            if c >= h: h_cnt += 1
        
        if h_cnt >= h: answer = h
        h += 1

    return answer