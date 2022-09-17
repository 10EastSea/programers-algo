# 폰켓몬
def solution(nums):
    answer = 0
    
    cnt_kinds, half_cnt_nums = len(set(nums)), len(nums) // 2
    if half_cnt_nums > cnt_kinds: answer = cnt_kinds
    else: answer = half_cnt_nums
    
    return answer