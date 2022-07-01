# 도둑질
def solution(money):
    answer = 0
    
    # 원형 탐색으로 인해 두가지 경우로 나누어 진행
    money1 = [0] + money[:-1] # 1. 첫번째 집을 선택하고, 마지막 집을 선택하지 않는 경우
    money2 = [0] + money[1:]  # 2. 마지막 집을 선택하고, 첫번째 집을 선택하지 않는 경우
    
    for i in range(2, len(money)):
        # i번째 집까지 중 최대값 = max(i번째 집을 선택하고 i-2번째 집에서의 최대값의 합, i-1번째 집에서의 최대값)
        money1[i] = max(money1[i] + money1[i-2], money1[i-1])
        money2[i] = max(money2[i] + money2[i-2], money2[i-1])
    
    # 두가지 경우 중 최대값
    answer = max(money1[-1], money2[-1])
    
    return answer