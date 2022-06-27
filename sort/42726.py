# 가장 큰 수
from functools import cmp_to_key

def custom_sort(a, b):
    a_b, b_a = str(a)+str(b), str(b)+str(a)
    if a_b < b_a: return 1
    elif a_b > b_a: return -1
    else: return 0


def solution(numbers):
    answer = ''

    numbers = sorted(numbers, key=cmp_to_key(custom_sort))
    answer = ''.join(map(lambda x: str(x), numbers))
    answer = str(int(answer))

    return answer