# 위장
from functools import reduce

def solution(clothes):
    answer = 0

    clothes_dict = {}
    for c in clothes:
        c_name, c_type = c[0], c[1]
        c_cnt = clothes_dict.get(c_type)
        if c_cnt is None: clothes_dict[c_type] = 1
        else: clothes_dict[c_type] = c_cnt + 1
    
    tmp = 1
    clothes_count_list = clothes_dict.values()
    for c in clothes_count_list: tmp *= (c+1)
    answer = tmp - 1

    return answer