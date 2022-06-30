# 카펫
import math

def get_candidates(num):
    result = []
    for n in range(3, int(math.sqrt(num))+1):
        if num % n == 0: result.append((num//n, n))
    return result

def solution(brown, yellow):
    answer = []

    area = brown + yellow
    candidates = get_candidates(area)

    for candidate in candidates:
        num1, num2 = candidate
        if brown == (num1)*2 + (num2-2)*2:
            answer = [num1, num2]
            break

    return answer