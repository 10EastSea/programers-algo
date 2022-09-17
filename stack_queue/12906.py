# 같은 숫자는 싫어
def solution(arr):
    answer = [arr[0]]
    
    idx_answer = 0
    for i in range(1, len(arr)):
        if arr[i] == answer[idx_answer]: continue
        else: answer.append(arr[i]); idx_answer += 1
    
    return answer