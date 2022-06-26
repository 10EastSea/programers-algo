# N으로 표현
def solution(N, number):
    answer = -1

    # {1: 1개로 만들 수 있는 수들, 2: 2개로 만들 수 있는 수들}
    can_create = {1: [N], 2: [int(str(N)*2), N+N, N-N, N*N, int(N/N)]}

    for i in range(3, 9): # 3 ~ 8
        can_create[i] = [int(str(N)*i)]
        for j in range(1, i):
            left, right = can_create[i - j], can_create[j]
            
            for l in left:
                for r in right:
                    can_create[i].append(l+r)
                    can_create[i].append(l-r)
                    can_create[i].append(l*r)
                    if r != 0: can_create[i].append(int(l/r))
        can_create[i] = list(set(can_create[i]))

    for key, value in can_create.items():
        if number in value:
            answer = key
            break
    return answer