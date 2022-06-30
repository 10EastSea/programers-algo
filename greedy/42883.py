# 큰 수 만들기
def solution(number, k):
    answer = ''

    result, delete_cnt = [],  0
    for n in number:
        if not result: result.append(n); continue
        elif delete_cnt == k: result.append(n); continue

        while result and delete_cnt < k:
            tmp = result.pop()
            if n > tmp: delete_cnt += 1
            else: result.append(tmp); break
        result.append(n)

    while delete_cnt < k: result.pop(); delete_cnt += 1

    answer = ''.join(result)
    return answer