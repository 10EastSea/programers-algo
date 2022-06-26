# 입국 심사
def solution(n, times):
    answer = 0

    start = min(times)
    end = max(times) * n
    while start < end:
        mid = int((start+end) / 2)
        tmp = sum(list(map(lambda x: int(mid/x), times)))
        if tmp >= n: end = mid
        else: start = mid + 1
    answer = start

    return answer