# k진수에서 소수 개수 구하기
import math

def is_prime(num):
    check = True
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0: check = False; break
    return check

def solution(n, k):
    answer = 0
    
    n_decimal = []
    while n > 0:
        n_decimal.append(str(n%k))
        n = n // k
    n_decimal.reverse()
    # print(''.join(n_decimal).split('0'))
    
    for num_str in ''.join(n_decimal).split('0'):
        if len(num_str) == 0 or num_str == '1': continue
        num = int(num_str)
        if is_prime(num): answer += 1
        # print(num, is_prime(num))
    
    return answer