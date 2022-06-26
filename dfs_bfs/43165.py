# 타겟 넘버
import copy

def solution(numbers, target):
    answer = 0

    result = [numbers[0], numbers[0]*(-1)]
    for n in numbers[1:]:
        tmp = []
        tmp.extend(list(map(lambda x: x+n, result)))
        tmp.extend(list(map(lambda x: x-n, result)))
        result = copy.deepcopy(tmp)
    answer = result.count(target)

    return answer