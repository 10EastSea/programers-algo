# 소수 찾기
from itertools import permutations
import math

def is_prime_num(number):
    if number == 0 or number == 1: return False
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0: return False
    return True

def solution(numbers):
    answer = 0

    results = set()
    for i in range(1, len(numbers)+1):
        candidates = list(permutations(numbers, i))
        for candidate in candidates:
            number = int(''.join(candidate))
            # print(number, is_prime_num(number))
            if is_prime_num(number): results.add(number)
    answer = len(results)

    return answer